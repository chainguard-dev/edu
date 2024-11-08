<?php

declare(strict_types=1);

test('default command "demo" is correctly loaded', function (): void {
    $app = getApp();
    $app->runCommand(['minicli', 'demo']);
})->expectOutputRegex("/help/");

test('the "demo test" command echoes command parameters', function (): void {
    $app = getApp();
    $app->runCommand(['minicli', 'demo', 'test', 'user=erika']);
})->expectOutputRegex("/erika/");

test('the "demo table" command prints test table', function (): void {
    $app = getApp();
    $app->runCommand(['minicli', 'demo', 'table']);
})->expectOutputRegex("/Header 3/");
