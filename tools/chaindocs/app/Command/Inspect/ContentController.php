<?php

declare(strict_types=1);

namespace App\Command\Inspect;

use App\AutodocsController;
use App\CatalogItem;
use App\Exception\InvalidTimestampException;
use App\InspectorService;
use Minicli\Output\Filter\ColorOutputFilter;

class ContentController extends AutodocsController
{
    public function handle(): void
    {
        $articlePath = $this->getArgs()[3] ?? null;

        if (!$articlePath) {
            $this->error('Please provide the path to a valid markdown file.');
            return;
        }

        $this->info("Inspecting article $articlePath");
        $article = new CatalogItem();
        try {
            $article->load($articlePath);
        } catch (InvalidTimestampException $e) {
        }

        /** @var InspectorService $inspector */
        $inspector = $this->getApp()->inspector;
        if ($inspector->inspect($article) === false) {;
            $this->error('Content failed inspection checks. Summary below:');
            $this->out($inspector->getSummary());
            return;
        }

        $this->success('Content passed inspection checks.');
        return;
    }
}
