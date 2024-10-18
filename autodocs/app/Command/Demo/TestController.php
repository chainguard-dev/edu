<?php

declare(strict_types=1);

namespace App\Command\Demo;

use Minicli\Command\CommandController;

class TestController extends CommandController
{
    public function handle(): void
    {
        $name = $this->hasParam('user') ? $this->getParam('user') : 'World';
        $this->display(sprintf("Hello, %s!", $name));

        print_r($this->getParams());
    }
}
