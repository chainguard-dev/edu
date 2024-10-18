<?php

declare(strict_types=1);

return [
    /****************************************************************************
     * Application Settings
     * --------------------------------------------------------------------------
     *
     * These are the core settings for your application.
     *****************************************************************************/

    'app_name' => envconfig(
        'MINICLI_APP_NAME',
        '
███╗   ███╗██╗███╗   ██╗██╗ ██████╗██╗     ██╗
████╗ ████║██║████╗  ██║██║██╔════╝██║     ██║
██╔████╔██║██║██╔██╗ ██║██║██║     ██║     ██║
██║╚██╔╝██║██║██║╚██╗██║██║██║     ██║     ██║
██║ ╚═╝ ██║██║██║ ╚████║██║╚██████╗███████╗██║
╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝╚══════╝╚═╝

Minimalist, dependency-free framework for building CLI-centric PHP applications'
    ),

    'app_path' => [
        __DIR__.'/../app/Command',
        '@minicli/command-help'
    ],

    'theme' => '',

    'debug' => true,

    ############################################################################
    # Librarian Configuration
    ############################################################################
    'data_path' => __DIR__ . '/../../content',
    'cache_path' => sys_get_temp_dir() . '/minicli-cache',
];
