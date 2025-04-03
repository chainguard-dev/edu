<?php

declare(strict_types=1);

namespace App;

use App\Command\CatalogItem;
use Minicli\Command\CommandController;
use Minicli\Output\Helper\TableHelper;

abstract class AutodocsController extends CommandController
{
    public CatalogService $catalog;

    public function unquote(string $string): string
    {
        return trim($string, '"');
    }

    public function getArticlesList(array $items): TableHelper
    {
        $table = new TableHelper();
        $table->addHeader(['Title', 'Last Updated']);

        /** @var CatalogItem $item */
        foreach ($items as $item) {
            $lastmod = $item->lastmod ? $item->lastmod->format('F jS, Y') : 'N/A';
            if ($item->content->frontMatterHas('title')) {
                $table->addRow([$this->unquote($item->routes[0]), $lastmod]);
            }
        }

        return $table;
    }

    public function getCsv(array $items): string
    {
        $csv = "Title,Last Updated\n";

        /** @var CatalogItem $item */
        foreach ($items as $item) {
            $lastmod = $item->lastmod ? $item->lastmod->format('Y-m-d') : 'N/A';
            if ($item->content->frontMatterHas('title')) {
                $csv .= $this->unquote($item->routes[0]).','.$lastmod."\n";
            }
        }

        return $csv;
    }

    public function getTopContentCsv(array $items): string
    {
        $csv = "Title, Views, Last Updated\n";

        foreach ($items as $content) {
            $item = $content['item'];
            $lastmod = $item->lastmod ? $item->lastmod->format('Y-m-d') : 'N/A';
            if ($item->content->frontMatterHas('title')) {
                $csv .= $this->unquote($item->routes[0]).','.$content['views'].','.$lastmod."\n";
            }
        }

        return $csv;
    }

    public function buildCatalog(bool $verbose = false): void
    {
        if ($verbose) {
            $this->out('Building content catalog...');
        }
        /** @var CatalogService $catalog */
        $this->catalog = $this->getApp()->catalog;
        if ($verbose) {
            $this->info('Catalog built with '.count($this->catalog->getAll()).' items.');
        }
    }
}
