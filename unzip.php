<?php
/**
 * KUNETT Hardware Auto-Deployer
 * Extracts kunett_update_11nov.zip directly into public_html
 */
$zipFile = __DIR__ . '/kunett_update_11nov.zip';

if (!file_exists($zipFile)) {
    die("<h2 style='color:red;'>❌ Error: kunett_update_11nov.zip not found in " . __DIR__ . "</h2><p>Please upload kunett_update_11nov.zip to public_html first.</p>");
}

$zip = new ZipArchive;
$res = $zip->open($zipFile);

if ($res === TRUE) {
    $zip->extractTo(__DIR__);
    $zip->close();
    
    echo "<div style='font-family:sans-serif; max-width:600px; margin:40px auto; padding:24px; border:2px solid #22c55e; border-radius:12px; background:#f0fdf4;'>";
    echo "<h2 style='color:#15803d; margin-top:0;'>✅ All 7 Agent-Readiness Fixes Extracted Successfully!</h2>";
    echo "<ul style='color:#166534; line-height:1.8;'>";
    echo "<li><strong>Goal 1:</strong> robots.txt with Content-Signal declared</li>";
    echo "<li><strong>Goal 2:</strong> about.html, terms.html, and homepage links</li>";
    echo "<li><strong>Goal 3:</strong> llms.txt strictly well-formed</li>";
    echo "<li><strong>Goal 4:</strong> .htaccess & index.md serving text/markdown</li>";
    echo "<li><strong>Goal 5:</strong> RFC 8288 Link headers on all responses</li>";
    echo "<li><strong>Goal 6:</strong> WebMCP tools exposed in head & forms</li>";
    echo "<li><strong>Goal 7:</strong> /.well-known/mcp/server-card.json published</li>";
    echo "</ul>";
    echo "<p style='color:#333; margin-bottom:0;'><strong>Next Step:</strong> You can now delete <code>unzip.php</code> from Hostinger File Manager.</p>";
    echo "</div>";
} else {
    echo "<h2 style='color:red;'>❌ Failed to extract zip file. Error code: $res</h2>";
}
?>