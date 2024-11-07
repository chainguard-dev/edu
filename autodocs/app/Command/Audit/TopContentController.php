<?php

namespace App\Command\Audit;

use App\AutodocsController;
use App\CatalogService;
use Minicli\Output\Filter\ColorOutputFilter;
use Parsed\Content;
use Parsed\ContentParser;

class TopContentController extends AutodocsController
{

    public function handle(): void
    {
        $this->buildCatalog();

        //ingest CSV from analytics
        if (!$this->hasParam('data')) {
            $this->error('Please provide a CSV file with analytics data.');
            return;
        }

        $path = $this->getParam('data');
        if  (!is_file($path)) {
            $this->error('File not found: ' . $path);
            return;
        }

        $count = 0;
        $needsUpdate = [];
        $skipRows = $this->hasParam('skip') ? $this->getParam('skip') : 8; //skip header rows

        if (($handle = fopen($path, "r")) !== FALSE) {
            while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
                $count++;
                if  ($count <= $skipRows) {
                    continue;
                }

                if ($data[0] === null) {
                    continue;
                }

                //locate article in catalog
                $this->info("Checking article: " . $data[0]);
                $item = $this->catalog->findByRoute($data[0]);
                $now = new \DateTimeImmutable();
                if ($item and $item->lastmod instanceof \DateTimeInterface) {
                    if ($now->diff($item->lastmod)->m > CatalogService::$DEPRECATION_CAP) {
                        $needsUpdate[] = $item;
                    }
                }

            }
            fclose($handle);
        }

        $this->info("Found " . count($needsUpdate) . " articles in the top $count that need updating.");
        $table = $this->getArticlesList($needsUpdate);
        $this->rawOutput($table->getFormattedTable(new ColorOutputFilter()));
        $this->newline();
    }
}
