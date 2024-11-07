<?php

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
                //$table->addRow([$this->unquote($item->content->frontMatterGet('title')), $lastmod_string]);
                $table->addRow([$this->unquote($item->routes[0]), $lastmod]);
            }
        }

        return $table;
    }

    public function buildCatalog(bool $verbose = false): void
    {
        if ($verbose) $this->out('Building content catalog...');
        /** @var CatalogService $catalog */
        $this->catalog = $this->getApp()->catalog;
        if ($verbose) $this->info('Catalog built with ' . count($this->catalog->getAll()) . ' items.');
    }
}
