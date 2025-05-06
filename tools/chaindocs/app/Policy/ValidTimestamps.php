<?php

namespace App\Policy;

use App\CatalogItem;
use App\PolicyInterface;

class ValidTimestamps implements PolicyInterface
{
    public array $results = [];

    public function verify(CatalogItem $item): bool
    {
        if (null === $item->lastmod) {
            $invalid = $item->getRaw('lastmod') ?? "Undefined";
            $this->results[] = "Invalid timestamp for 'lastmod' field: $invalid";
        }

        if (null === $item->created) {
            $invalid = $item->getRaw('date') ?? "Undefined";
            $this->results[] = "Invalid timestamp for 'date' field: $invalid";
        }

        return count($this->results) === 0;
    }
}
