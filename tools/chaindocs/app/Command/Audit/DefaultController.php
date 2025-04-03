<?php

declare(strict_types=1);

namespace App\Command\Audit;

use App\AutodocsController;
use Minicli\Output\Filter\ColorOutputFilter;

class DefaultController extends AutodocsController
{
    public function handle(): void
    {
        $this->buildCatalog(true);
        $this->error('Found '.count($this->catalog->getInvalid()).' articles with invalid timestamps.');
        $this->error('Found '.count($this->catalog->getDeprecated()).' articles not updated in the last 7 months.');
        $this->newline();

        if ($this->hasFlag('invalid')) {
            $table = $this->getArticlesList($this->catalog->getInvalid());
            $this->out('Articles with invalid timestamps:');
            $this->rawOutput($table->getFormattedTable(new ColorOutputFilter()));
            $this->newline();
        }

        if ($this->hasFlag('deprecated')) {
            $table = $this->getArticlesList($this->catalog->getDeprecated());
            $this->out('Articles last updated > 7 months ago:');
            $this->rawOutput($table->getFormattedTable(new ColorOutputFilter()));
            $this->newline();
        }
    }
}
