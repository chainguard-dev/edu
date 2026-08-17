// On linux npm links .bin/sass to pure-JS sass (can't run --embedded), breaking Hugo's Dart Sass — force the link to sass-embedded's shim and set the exec bit.
const fs = require("fs");
const path = require("path");

const binDir = path.join(__dirname, "..", "node_modules", ".bin");
const target = path.join("..", "sass-embedded", "dist", "bin", "sass.js");
const link = path.join(binDir, "sass");

fs.chmodSync(path.resolve(binDir, target), 0o755);
fs.rmSync(link, { force: true });
fs.symlinkSync(target, link);
console.log(`link-dart-sass: ${link} -> ${target}`);
