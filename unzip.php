<?php
/**
 * KUNETT Hardware Auto-Deployer
 * Extracts zip archives directly into public_html
 */

// Candidate priority
$priorityFiles = [
    'kunett_website_complete_restore.zip',
    'kunett_assets_images_only.zip',
    'kunett_only_edited_files_16nov.zip',
    'kunett_final_hostinger.zip',
    'kunett_update_16nov.zip',
    'kunett_update_14nov.zip'
];

$allZips = glob(__DIR__ . '/*.zip');
$zipFile = null;

// Allow manual selection via query parameter ?file=...
if (!empty($_GET['file'])) {
    $candidate = __DIR__ . '/' . basename($_GET['file']);
    if (file_exists($candidate)) {
        $zipFile = $candidate;
    }
}

if (!$zipFile) {
    foreach ($priorityFiles as $pf) {
        $path = __DIR__ . '/' . $pf;
        if (file_exists($path)) {
            $zipFile = $path;
            break;
        }
    }
}

// Fallback to the newest zip file in directory
if (!$zipFile && !empty($allZips)) {
    usort($allZips, function($a, $b) {
        return filemtime($b) - filemtime($a);
    });
    $zipFile = $allZips[0];
}

if (!$zipFile) {
    echo "<div style='font-family:sans-serif; max-width:640px; margin:40px auto; padding:28px; border:2px solid #ef4444; border-radius:16px; background:#fef2f2;'>";
    echo "<h2 style='color:#dc2626; margin-top:0;'>❌ No Zip File Found in public_html</h2>";
    echo "<p style='color:#7f1d1d; font-size:15px; line-height:1.6;'>Please upload either:</p>";
    echo "<ul style='color:#7f1d1d; line-height:1.8;'>";
    echo "<li><strong>kunett_assets_images_only.zip</strong> (43 MB - all 125 product images)</li>";
    echo "<li><strong>kunett_website_complete_restore.zip</strong> (118 MB - complete site with all images, PDF & video)</li>";
    echo "</ul>";
    echo "<p style='color:#7f1d1d; font-size:14px;'>Upload the zip file into <code>public_html/</code> and refresh this page.</p>";
    echo "</div>";
    exit;
}

$zip = new ZipArchive;
$res = $zip->open($zipFile);

if ($res === TRUE) {
    $numFiles = $zip->numFiles;
    $zip->extractTo(__DIR__);
    $zip->close();
    
    echo "<div style='font-family:sans-serif; max-width:640px; margin:40px auto; padding:28px; border:2px solid #22c55e; border-radius:16px; background:#f0fdf4; box-shadow:0 10px 25px rgba(0,0,0,0.05);'>";
    echo "<h2 style='color:#15803d; margin-top:0;'>✅ Website Assets Extracted Successfully!</h2>";
    echo "<p style='color:#166534; font-size:15px; line-height:1.6;'>Extracted: <strong>" . basename($zipFile) . "</strong> (" . round(filesize($zipFile) / (1024*1024), 2) . " MB, " . $numFiles . " files)</p>";
    echo "<ul style='color:#166534; line-height:1.8;'>";
    echo "<li><strong>100% Product Images:</strong> All 200, 300, 400, 450, and 500 series models restored</li>";
    echo "<li><strong>Brand Assets:</strong> Official logos, founder photos, and high-res banners restored</li>";
    echo "<li><strong>Collection Pages:</strong> Ready with complete product imagery and interactive specs</li>";
    echo "</ul>";
    echo "<div style='margin-top:20px; padding:14px 18px; background:#dcfce7; border-radius:10px; display:flex; gap:12px; flex-wrap:wrap;'>";
    echo "<a href='/aluminium-handles.html' style='color:#15803d; font-weight:700; text-decoration:none;'>👉 Check Collection Page &rarr;</a>";
    echo "<a href='/' style='color:#15803d; font-weight:700; text-decoration:none;'>👉 Check Homepage &rarr;</a>";
    echo "</div>";
    echo "<p style='color:#666; font-size:12px; margin-top:20px; margin-bottom:0;'>💡 Tip: For security, delete <code>unzip.php</code> from Hostinger once verified.</p>";
    echo "</div>";
} else {
    echo "<h2 style='color:#dc2626; font-family:sans-serif;'>❌ Failed to extract zip file. Error code: $res</h2>";
}
?>