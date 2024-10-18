<?php

namespace App;

use Minicli\App;
use Minicli\ServiceInterface;
use Parsed\Content;
use Parsed\ContentParser;

class CatalogService implements ServiceInterface
{
    protected ContentParser $contentParser;

    protected string $dataPath;

    /** @var Content[] */
    protected array $catalog = [];

    /** @var array */
    protected array $deprecated = [];

    /** @var array */
    protected array $invalid = [];

    /** @var array */
    protected array $updated = [];

    public function load(App $app): void
    {
        $this->dataPath = $app->config->data_path;
        $this->contentParser = new ContentParser();
        $this->buildCatalog($this->dataPath, $this->contentParser);
    }

    public function buildCatalog(string $path, ContentParser $contentParser): void
    {
        foreach (glob($path . '/*') as $path) {
            if (is_dir($path)) {
                $this->buildCatalog($path, $contentParser);
            }

            if (pathinfo($path, PATHINFO_EXTENSION) !== 'md') {
                continue;
            }

            $article = $contentParser->parse(new Content(file_get_contents($path)));
            $this->audit($article);
            $this->catalog[] = $article;
        }
    }

    public function getAll(): array
    {
        return $this->catalog;
    }

    public function audit(Content $content): void
    {
        $timestamp = $content->frontMatterHas('lastmod') ? $content->frontMatterGet('lastmod') : $content->frontMatterGet('date');
        if (!$timestamp) {
            $this->invalid[] = $content;
            return;
        }
        try  {
            $lastmod = new \DateTime($timestamp);
            $now = new \DateTime();
        } catch (\Exception $e) {
            $this->invalid[] = $content;
            return;
        }

        if ($now->diff($lastmod)->m > 7) {
            $this->deprecated[] = [ 'content' => $content, 'lastmod' => $lastmod ];
            return;
        }

        $this->updated[] = [ 'content' => $content, 'lastmod' => $lastmod ];
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
        $result = [];
        $this->orderByLastMod($audit);
        foreach ($audit as $item) {
            $result[] = $item['content'];
        }

        return $result;
    }
    protected function orderByLastMod(array &$array): void
    {
        usort($array, function ($a, $b) {
            return $a['lastmod'] <=> $b['lastmod'];
        });
    }
}
