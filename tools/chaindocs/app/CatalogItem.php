<?php

declare(strict_types=1);

namespace App;

use App\Exception\InvalidTimestampException;
use DateTimeImmutable;
use DateTimeInterface;
use Exception;
use Parsed\Content;
use Parsed\ContentParser;

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

        $createdTs = $this->content->frontMatterGet('date');
        #$updatedTs = $this->content->frontMatterHas('lastmod') ? $this->content->frontMatterGet('lastmod') : $createdTs;
        $updatedTs = $this->content->frontMatterGet('lastmod') ?: null;

        if ($createdTs === null) {
            throw new InvalidTimestampException("Invalid timestamp for 'date' field: {$createdTs}");
        }

        if ($updatedTs === null) {
            throw new InvalidTimestampException("Invalid timestamp for 'lastmod' field: {$updatedTs}");
        }

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

    public function getRaw(string $key): string | null
    {
        return $this->content->frontMatterHas($key) ? $this->content->frontMatterGet($key) : null;
    }
}
