<?php

namespace App\Command\Audit;

use App\AutodocsController;
use App\CatalogService;
use App\Command\CatalogItem;
use Minicli\FileNotFoundException;
use Minicli\Output\Filter\ColorOutputFilter;
use Minicli\Output\Helper\TableHelper;
use Parsed\Content;
use Parsed\ContentParser;

class TopContentController extends AutodocsController
{

    public function handle(): void
    {
        $this->buildCatalog();

        if (!$this->hasParam('data')) {
            $this->error('Please provide a "data=your-file.csv" param with a CSV file containing analytics data.');
            return;
        }

        $path = $this->getParam('data');
        if  (!is_file($path)) {
            $this->error('File not found: ' . $path);
            return;
        }

        try {
            $this->catalog->ingestAnalytics($path);
            $deprecated = $this->hasFlag('deprecated') ? CatalogService::$DEPRECATION_CAP : null;
            $topContent = $this->catalog->getTopContent($deprecated);

        } catch (FileNotFoundException $e) {
            $this->error('Error reading CSV file: ' . $e->getMessage());
            return;
        }

        $table = new TableHelper();
        $table->addHeader(['Title', 'Views', 'Last Updated']);

        foreach ($topContent as $content) {
            $item = $content['item'];
            $lastmod = $item->lastmod ? $item->lastmod->format('F jS, Y') : 'N/A';
            if ($item->content->frontMatterHas('title')) {
                $table->addRow([$this->unquote($item->routes[0]), $content['views'], $lastmod]);
            }
        }

        $this->rawOutput($table->getFormattedTable(new ColorOutputFilter()));
        $this->newline();
    }
}
