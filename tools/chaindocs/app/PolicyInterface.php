<?php

namespace App;

interface PolicyInterface
{
    public function verify(CatalogItem $item): bool;
}
