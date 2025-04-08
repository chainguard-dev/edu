<?php

declare(strict_types=1);

namespace App;

use DateTime;
use DateTimeImmutable;
use DateTimeInterface;
use Minicli\App;
use Minicli\FileNotFoundException;
use Minicli\ServiceInterface;
use Parsed\ContentParser;
use App\Exception\InvalidTimestampException;

class CatalogService implements ServiceInterface
{
    protected ContentParser $contentParser;

    protected string $dataPath;

    /** @var CatalogItem[] */
    protected array $catalog = [];

    /** @var CatalogItem[] */
    protected array $deprecated = [];

    /** @var CatalogItem[] */
    protected array $invalid = [];

    /** @var CatalogItem[] */
    protected array $updated = [];

    protected array $topContent = [];

    public static int $DEPRECATION_CAP = 7;

    public function load(App $app): void
    {
        $this->dataPath = $app->config->data_path;
        $this->buildCatalog($this->dataPath);
    }

    public function buildCatalog(string $path): void
    {
        foreach (glob($path.'/*') as $path) {
            if (is_dir($path)) {
                $this->buildCatalog($path);
            }

            if ('md' !== pathinfo($path, PATHINFO_EXTENSION)) {
                continue;
            }

            if ('_index.md' === basename($path)) {
                continue;
            }

            $item = new CatalogItem();
            try {
                $item->load($path);
            } catch (InvalidTimestampException $e) {

            }
            $this->audit($item);
            $this->catalog[] = $item;
        }
    }

    public function getAll(): array
    {
        return $this->catalog;
    }

    public function audit(CatalogItem $item): void
    {
        if (null === $item->lastmod) {
            $this->invalid[] = $item;
            return;
        }

        $now = new DateTime();
        if ($now->diff($item->lastmod)->m > self::$DEPRECATION_CAP) {
            $this->deprecated[] = $item;
            return;
        }

        $this->updated[] = $item;
    }

    public function getDeprecated(): array
    {
        return $this->getAudited($this->deprecated);
    }

    public function getInvalid(): array
    {
        return $this->getAudited($this->invalid);
    }

    public function getUpdated(): array
    {
        return $this->getAudited($this->updated);
    }

    protected function getAudited(array $audit): array
    {
        $this->orderByLastMod($audit);

        return $audit;
    }
    protected function orderByLastMod(array &$array): void
    {
        usort($array, fn ($a, $b) => $a->lastmod <=> $b->lastmod);
    }

    public function findByRoute(string $route): ?CatalogItem
    {
        foreach ($this->catalog as $item) {
            if (in_array($route, $item->routes)) {
                return $item;
            }
        }

        return null;
    }

    /**
     * @throws FileNotFoundException
     */
    public function ingestAnalytics(string $inputCsv, int $skipRows = 8): void
    {
        if ( ! is_file($inputCsv)) {
            throw new FileNotFoundException('File not found: '.$inputCsv);
        }

        $count = 0;

        /**
         * data[0]: Route
         * data[1]: Views
         * data[2]: Active Users
         * data[3]: Views per Active User
         * data[4]: Event count
         * data[5]: Bounce Rate
         */

        if (($handle = fopen($inputCsv, "r")) !== false) {
            while (($data = fgetcsv($handle, 1000, ",")) !== false) {
                $count++;
                if ($count <= $skipRows) {
                    continue;
                }

                if (null === $data[0]) {
                    continue;
                }

                $item = $this->findByRoute($data[0]);
                if ($item && $item->lastmod instanceof DateTimeInterface) {
                    $this->topContent[] = ['item' => $item, 'views' => $data[1], 'active_users' => $data[2], 'views_per_user' => $data[3], 'event_count' => $data[4], 'bounce_rate' => $data[5]];
                }
            }
            fclose($handle);
        }

    }

    public function getTopContent(?int $olderThanMonths = null): array
    {
        if ( ! $olderThanMonths) {
            return $this->topContent;
        }

        $topContent = [];
        foreach ($this->topContent as $content) {
            $now = new DateTimeImmutable();
            if ($now->diff($content['item']->lastmod)->m > $olderThanMonths) {
                $topContent[] = $content;
            }
        }
        return $topContent;
    }
}
