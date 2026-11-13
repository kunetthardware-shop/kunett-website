<?php
/**
 * KUNETT Hardware Auto-Deployer
 * Extracts kunett_final_hostinger.zip or kunett_update_11nov.zip directly into public_html
 */
$candidates = [
    __DIR__ . '/kunett_final_hostinger.zip',
    __DIR__ . '/kunett_update_11nov.zip'
];

$zipFile = null;
foreach ($candidates as $cand) {
    if (file_exists($cand)) {
        $zipFile = $cand;
        break;
    }
}

if (!$zipFile) {
    die("<h2 style='color:#e11d48; font-family:sans-serif;'>❌ Error: No zip file found in " . htmlspecialchars(__DIR__) . "</h2><p style='font-family:sans-serif;'>Please upload <strong>kunett_final_hostinger.zip</strong> to <code>public_html/</code> and refresh this page.</p>");
}

$zip = new ZipArchive;
$res = $zip->open($zipFile);

if ($res === TRUE) {
    $zip->extractTo(__DIR__);
    $zip->close();
    
    echo "<div style='font-family:sans-serif; max-width:640px; margin:40px auto; padding:28px; border:2px solid #22c55e; border-radius:16px; background:#f0fdf4; box-shadow:0 10px 25px rgba(0,0,0,0.05);'>";
    echo "<h2 style='color:#15803d; margin-top:0;'>✅ Website Updated Successfully!</h2>";
    echo "<p style='color:#166534; font-size:15px; line-height:1.6;'>Extracted: <strong>" . basename($zipFile) . "</strong> (" . round(filesize($zipFile) / (1024*1024), 2) . " MB)</p>";
    echo "<ul style='color:#166534; line-height:1.8;'>";
    echo "<li><strong>Aluminium Handles (200 Series):</strong> Modern luxury header & floating glass pill nav</li>";
    echo "<li><strong>Interactive Slider:</strong> Smooth touch/drag scrolling + prev/next buttons + direct card navigation</li>";
    echo "<li><strong>Collection Pages:</strong> Direct <code>#card-XXX</code> hash jumping with highlight animation</li>";
    echo "<li><strong>Mobile Responsive:</strong> Fixed sticky navigation & scroll locking across all views</li>";
    echo "<li><strong>Cache Headers:</strong> Real-time fresh HTML delivery (no stale cache)</li>";
    echo "</ul>";
    echo "<div style='margin-top:20px; padding:12px 16px; background:#dcfce7; border-radius:8px;'>";
    echo "<a href='/aluminium-handles.html' style='color:#15803d; font-weight:700; text-decoration:none;'>👉 Open aluminium-handles.html to verify &rarr;</a>";
    echo "</div>";
    echo "<p style='color:#666; font-size:12px; margin-top:20px; margin-bottom:0;'>💡 Tip: For best security, you may delete <code>unzip.php</code> from Hostinger File Manager once verified.</p>";
    echo "</div>";
} else {
    echo "<h2 style='color:#e11d48; font-family:sans-serif;'>❌ Failed to extract zip file. Error code: $res</h2>";
}
?>