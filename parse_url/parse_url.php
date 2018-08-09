<?php declare(strict_types=1);

$fwp = __DIR__ . '/php_urls.json';

$jsonLoad = file_get_contents($fwp);
$jsonObject = json_decode($jsonLoad);

$dataArray = [];
foreach ($jsonObject as $url => $data) {
    $dataArray[$url] = parse_url($url);
}

$jsonData = json_encode($dataArray, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
if ($jsonData) {
    file_put_contents($fwp, $jsonData);
} else {
    echo json_last_error_msg();
}
