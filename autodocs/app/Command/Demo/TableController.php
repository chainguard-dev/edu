<?php

declare(strict_types=1);

namespace App\Command\Demo;

use Minicli\Command\CommandController;
use Minicli\Output\Filter\ColorOutputFilter;
use Minicli\Output\Helper\TableHelper;

class TableController extends CommandController
{
    public function handle(): void
    {
        $this->display('Testing Tables');

        $table = new TableHelper();
        $table->addHeader(['Header 1', 'Header 2', 'Header 3']);

        for ($i = 1; $i <= 10; $i++) {
            $table->addRow([(string)$i, (string)rand(0, 10), "other string {$i}"]);
        }

        $this->newline();
        $this->rawOutput($table->getFormattedTable(new ColorOutputFilter()));
        $this->newline();
    }
}
