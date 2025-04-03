<?php

declare(strict_types=1);

namespace App\Command\Audit;

use App\AutodocsController;
use App\CatalogService;
use Minicli\FileNotFoundException;

class ReportController extends AutodocsController
{
    public function handle(): void
    {
        $this->buildCatalog(true);
        $this->error('Found '.count($this->catalog->getInvalid()).' articles with invalid timestamps.');
        $this->error('Found '.count($this->catalog->getDeprecated()).' articles not updated in the last 7 months.');
        $this->newline();
        $csv = '';

        if ($this->hasFlag('invalid')) {
            $csv = $this->getCsv($this->catalog->getInvalid());
        }

        if ($this->hasFlag('deprecated')) {
            $csv = $this->getCsv($this->catalog->getDeprecated());
        }

        if ($this->hasFlag('topcontent')) {
            if ( ! $this->hasParam('data')) {
                $this->error('Please provide a "data=your-file.csv" param with a CSV file containing analytics data.');
                return;
            }

            try {
                $this->catalog->ingestAnalytics($this->getParam('data'));
                $topContent = $this->catalog->getTopContent(CatalogService::$DEPRECATION_CAP);
                $csv = $this->getTopContentCsv($topContent);

            } catch (FileNotFoundException $e) {
                $this->error('Error reading CSV file: '.$e->getMessage());
                return;
            }
        }

        if ($this->hasParam('output')) {
            $this->info('Writing CSV to '.$this->getParam('output'));
            file_put_contents($this->getParam('output'), $csv);
            return;
        }

        $this->out($csv);
    }
}
