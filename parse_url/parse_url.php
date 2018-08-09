<?php declare(strict_types=1);

$rootDir = 'example_data';
$fileArray = ['url.http.json'];


function extract($rootDir, $filename)
{
    $parsedData = [];
    $f = file_get_contents(sprintf("%s/input/%s", $rootDir, $filename));
    foreach (json_decode($f) as $url) {
        $parsedData[$url] = parse_url($url);
    }
    return $parsedData;
}


function save($rootDir, $filename, $parsedData)
{
    $jsonData = json_encode($parsedData, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
    if ($jsonData) {
        file_put_contents(sprintf("%s/output/php/%s", $rootDir, $filename), $jsonData);
    } else {
        echo json_last_error_msg();
    }
}


foreach ($fileArray as $f) {
    $parsedData = extract($rootDir, $f);
    save($rootDir, $f, $parsedData);
}
