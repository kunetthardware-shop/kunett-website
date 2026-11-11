<?php
/**
 * KUNETT Hardware - Markdown Content Negotiation Handler
 * Serves lightweight Markdown representation for AI agents requesting Accept: text/markdown
 */
header("Content-Type: text/markdown; charset=utf-8");
header("Vary: Accept");
header('Link: </llms.txt>; rel="alternate"; type="text/markdown", </llms.txt>; rel="describedby", <https://kunetthardware.com/llms.txt>; rel="alternate"; type="text/markdown", </.well-known/mcp/server-card.json>; rel="service-desc"');
header("X-Content-Type-Options: nosniff");

$mdFile = __DIR__ . '/index.md';
if (file_exists($mdFile)) {
    readfile($mdFile);
} elseif (file_exists(__DIR__ . '/llms.txt')) {
    readfile(__DIR__ . '/llms.txt');
} else {
    echo "# KUNETT Hardware\n\n> Premier manufacturer of 100% solid aerospace-grade 6063-T5 aluminium architectural handles, continuous handle profiles, and concealed counsil hardware in Rajkot, Gujarat.\n\nWebsite: https://kunetthardware.com\nContact: +91 99246 37640\n";
}
exit;
?>