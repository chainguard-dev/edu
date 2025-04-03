<?php

declare(strict_types=1);

test('default command "help" is correctly loaded', function (): void {
    $app = getApp();
    $app->runCommand(['chaindocs', 'help']);
})->expectOutputRegex("/help/");
