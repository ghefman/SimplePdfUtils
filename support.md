# Simple Pdf Utils — Support

_Last updated: 2026-05-21_

Simple Pdf Utils is a fully on-device PDF editor for iPhone. This page is the place to ask questions or report bugs.

## Get in touch

📧 **Email:** [ghefetz@gmail.com](mailto:ghefetz@gmail.com)

Please include:

- Your iPhone model and iOS version (Settings → General → About).
- The app version (visible in the App Store listing).
- Steps to reproduce the problem.
- A screenshot if it's visual.

Because the app does not transmit any data, there are no server-side logs we can look up — your message is the only signal we have.

---

## Frequently asked

### How does the app stay completely offline?

The app contains no networking code. The embedded PDF rendering library runs inside a sandboxed WebView with a strict Content Security Policy (`connect-src 'none'`) that prevents any outgoing connection at the browser level. You can verify this yourself by enabling Airplane Mode — every feature works identically.

### Where do my files go when I tap **Save**?

To wherever you choose. The app hands the assembled PDF to the standard iOS share sheet. You then pick a destination — Files, Mail, iCloud Drive, Messages, etc. The app itself does not store, sync, or transmit your files.

### Why does compressing a page make it lose searchable text?

Compression rasterizes the page into a JPEG image. Text becomes pixels, so it can no longer be selected or searched. We made that explicit in the description — use compression only where text loss is acceptable (image-heavy scans, photo pages, etc.).

### Can I undo a compression?

Yes. Tap the same `↓` button again on a compressed page — it returns to the original.

### Why is the resulting page sometimes larger after compression?

Most pages are not photo-heavy. For a text-only page, the vector representation is already small; rasterizing it can produce a larger file. The compression button only appears for pages over 300 KB, where the savings are typically real.

### Does the app work with encrypted / password-protected PDFs?

The app tries to read encrypted PDFs in pass-through mode. If a PDF uses strong encryption that requires a password, opening it will likely fail. We don't currently support entering a password.

### Why doesn't the app appear in the iPad App Store?

v1.0 ships iPhone-only. iPad support may come in a later release.

---

## Privacy

The full privacy policy is here: [Privacy Policy](./privacy-policy)

Short version: the app does not collect, transmit, store, or share any data. It cannot reach the internet.

---

## Reporting a bug

If something genuinely doesn't work, email with:

1. **What you tried** (e.g., "Picked 3 PDFs, marked page 2 of file 1 to remove, tapped Save").
2. **What happened** (e.g., "App froze for 5 seconds, then no share sheet appeared").
3. **What you expected** (e.g., "Share sheet to appear immediately").

If the app actually crashed (closes back to the home screen), iOS keeps a crash log under **Settings → Privacy & Security → Analytics & Improvements → Analytics Data**. Find one starting with `pdfutils-` or `Simple Pdf Utils-` and attach its `.ips` file to the email.
