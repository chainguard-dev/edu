<?php

namespace App;

use App\Command\CatalogItem;
use Minicli\App;
use Minicli\ServiceInterface;
use Parsed\Content;
use Parsed\ContentParser;

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

    public static int $DEPRECATION_CAP = 7;

    public function load(App $app): void
    {
        $this->dataPath = $app->config->data_path;
        $this->buildCatalog($this->dataPath);
    }

    public function buildCatalog(string $path): void
    {
        foreach (glob($path . '/*') as $path) {
            if (is_dir($path)) {
                $this->buildCatalog($path);
            }

            if (pathinfo($path, PATHINFO_EXTENSION) !== 'md') {
                continue;
            }

            if (basename($path) === '_index.md') {
                continue;
            }

            $item = new CatalogItem();
            $item->load($path);
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
        if ($item->lastmod === null) {
            $this->invalid[] = $item;
            return;
        }

        $now = new \DateTime();
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
        usort($array, function ($a, $b) {
            return $a->lastmod <=> $b->lastmod;
        });
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
}
