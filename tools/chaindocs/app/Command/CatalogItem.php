<?php

declare(strict_types=1);

namespace App\Command;

use DateTimeInterface;
use Parsed\Content;
use Parsed\ContentParser;
use DateTimeImmutable;
use Exception;

class CatalogItem
{
    public Content $content;

    public string $path;

    public ?DateTimeInterface $lastmod = null;

    public ?DateTimeInterface $created = null;

    public array $routes = [];

    public function load(string $path): void
    {
        $this->path = $path;
        $contentParser = new ContentParser();
        $this->content = $contentParser->parse(new Content(file_get_contents($this->path)));
        $this->routes = $this->getRoutes();

        $createdTs = $this->content->frontMatterHas('date') ? $this->content->frontMatterGet('date') : date('Y-m-d H:i:s');
        $updatedTs = $this->content->frontMatterHas('lastmod') ? $this->content->frontMatterGet('lastmod') : $createdTs;

        try {
            $this->created = new DateTimeImmutable($createdTs);
            $this->lastmod = new DateTimeImmutable($updatedTs);
        } catch (Exception $e) {
        }
    }

    public function getRoutes(): array
    {
        $rpl = str_replace('.md', '', $this->path);
        $rpl = mb_substr($rpl, mb_strpos($rpl, 'content/') + 7);
        $rpl = str_replace('index', '', $rpl);

        $routes[] = $rpl;

        if ( ! str_ends_with($rpl, '/')) {
            $routes[] = $rpl.'/';
            $routes[] = $rpl.'/index.html';
        } else {
            $routes[] = mb_substr($rpl, 0, -1);
            $routes[] = $rpl.'index.html';
        }

        return $routes;
    }
}
