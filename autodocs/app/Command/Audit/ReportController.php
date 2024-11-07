<?php

declare(strict_types=1);

namespace App\Command\Audit;

use App\AutodocsController;
use App\CatalogService;
use Minicli\Output\Filter\ColorOutputFilter;

class ReportController extends AutodocsController
{
    public function handle(): void
    {
        // generate csv report
    }
}
