<?php

declare(strict_types=1);

use App\CatalogService;
use App\InspectorService;

return [
    /****************************************************************************
     * Application Services
     * --------------------------------------------------------------------------
     *
     * The services to be loaded for your application.
     *****************************************************************************/

    'services' => [
        'catalog' => CatalogService::class,
        'inspector' => InspectorService::class,
    ],
];
