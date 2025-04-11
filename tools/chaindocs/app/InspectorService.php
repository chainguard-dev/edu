<?php

namespace App;

use App\Policy\ValidTimestamps;
use Minicli\App;
use Minicli\ServiceInterface;

class InspectorService implements ServiceInterface
{
    /** @var PolicyInterface[]  */
    public array $policies = [];
    public array $errors = [];

    public function load(App $app): void
    {
        $this->addPolicy(new ValidTimestamps());
    }

    public function addPolicy(PolicyInterface $policy): void
    {
        $this->policies[] = $policy;
    }

    public function inspect(CatalogItem $item): bool
    {
        foreach ($this->policies as $policy) {
            if (!$policy->verify($item)) {
                foreach ($policy->results as $result) {
                    $this->errors[] = $result;
                }
            }
        }

        return count($this->errors) === 0;
    }

    public function getSummary(): string
    {
        $summary = '------------------------------' . PHP_EOL;
        $summary .= 'Total Checks: ' . count($this->policies) . PHP_EOL;
        $summary .= 'Errors Found: ' . count($this->errors) . PHP_EOL;
        $summary .= '------------------------------' . PHP_EOL;
        $summary .= 'Errors:' . PHP_EOL;
        foreach ($this->errors as $error) {
            $summary .= ' - ' . $error . PHP_EOL;
        }

        return $summary;
    }
}
