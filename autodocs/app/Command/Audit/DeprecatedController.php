<?php

declare(strict_types=1);

namespace App\Command\Audit;

use App\CatalogService;
use Minicli\Command\CommandController;
use Minicli\Output\Filter\ColorOutputFilter;
use Minicli\Output\Helper\TableHelper;

class DeprecatedController extends CommandController
{
    /**
     * @throws \Exception
     */
    public function handle(): void
    {
        /** @var CatalogService $catalog */
        $catalog = $this->getApp()->catalog;
        $deprecated = $catalog->getDeprecated();

        $this->info('Catalog built with ' . count($catalog->getAll()) . ' items.');
        $this->error('Found ' . count($deprecated) . ' articles last updated > 7 months ago:');
        $table = new TableHelper();
        $table->addHeader(['Title', 'Last Updated']);
        foreach ($deprecated as $item) {
            if ($item->frontMatterHas('title')) {
                $lastmod = new \DateTimeImmutable($item->frontMatterGet('lastmod'));
                $table->addRow([$this->unquote($item->frontMatterGet('title')), $lastmod->format('F jS, Y')]);
            }
        }

        $this->rawOutput($table->getFormattedTable(new ColorOutputFilter()));
        $this->newline();
    }

    public function unquote(string $string): string
    {
        return trim($string, '"');
    }
}
