# Simple Pdf Utils — Support

_Last updated: 2026-05-31_

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

The app contains no networking code. The embedded PDF rendering library runs inside a sandboxed WebView with a strict Content Security Policy (`connect-src 'none'`) that prevents any outgoing connection at the browser level. Word documents are converted using a local JavaScript library (mammoth) and the built-in iOS print engine — no cloud service is involved. You can verify everything works offline by enabling Airplane Mode.

### Where do my files go when I tap **Save**?

To wherever you choose. The app hands the assembled PDF to the standard iOS share sheet. You then pick a destination — Files, Mail, iCloud Drive, Messages, etc. The app itself does not store, sync, or transmit your files.

### How does Word document (.docx) conversion work?

When you add a .docx file, the app converts it to a PDF entirely on your device in two steps: first the document is parsed into HTML using the open-source mammoth library, then that HTML is rendered to a PDF using iOS's built-in print engine. No file ever leaves your device.

Because this process re-flows the content rather than preserving the exact page layout, complex formatting may look different or be missing — multi-column layouts, text boxes, precise page breaks, headers and footers, charts, and complex table styles are the most common cases. The app shows a warning whenever a Word file is added. For simple documents (paragraphs, headings, basic tables), the result is usually clean.

**.doc files** (the older Word format) are not supported and are silently excluded from the file picker.

### How do text annotations work?

Tap the **T** button on any page row to open the text editor. Type your text, choose a font, size, and colour, then tap **Add**. The annotation appears on the page thumbnail as a draggable dot — drag it to reposition. Tap an existing annotation to re-edit its text, font, size, or colour.

Annotations are baked into the page at export time (when you tap **Save**). They also show up in the full-screen page preview so you can check placement before saving. The text is rendered as real vector text in the exported PDF, so it remains selectable and searchable — it is not rasterized unless you also compress that page.

### Can I undo or remove an annotation?

Yes. Tap the **T** button again on the same row — the text editor opens with your existing annotations listed. You can edit or delete individual annotations from there.

### Does rotating a page change the original file?

No. The rotation is applied only to the exported PDF. Your source file on disk is never modified. If you remove the file from the list and re-add it, it comes in at its original orientation.

### Why does compressing a page make it lose searchable text?

Compression rasterizes the page into a JPEG image. Text becomes pixels, so it can no longer be selected or searched. Use compression only where text loss is acceptable — image-heavy scans, photo pages, etc.

### Can I undo a compression?

Yes. Tap the same `↓` button again on a compressed page — it returns to the original.

### Why is the resulting page sometimes larger after compression?

Most pages are not photo-heavy. For a text-only page, the vector representation is already small; rasterizing it can produce a larger file. The compression button only appears for pages already over 300 KB, where the savings are typically real.

### Does the app work with encrypted / password-protected PDFs?

The app tries to read encrypted PDFs in pass-through mode. If a PDF uses strong encryption that requires a password, opening it will likely fail. Password entry is not currently supported.

### Why doesn't the app appear in the iPad App Store?

The app currently ships iPhone-only. iPad support may come in a later release.

---

## Privacy

The full privacy policy is here: [Privacy Policy](privacy-policy.md)

Short version: the app does not collect, transmit, store, or share any data. It cannot reach the internet.

---

## Reporting a bug

If something genuinely doesn't work, email with:

1. **What you tried** (e.g., "Picked 3 PDFs, marked page 2 of file 1 to remove, tapped Save").
2. **What happened** (e.g., "App froze for 5 seconds, then no share sheet appeared").
3. **What you expected** (e.g., "Share sheet to appear immediately").

If the app actually crashed (closes back to the home screen), iOS keeps a crash log under **Settings → Privacy & Security → Analytics & Improvements → Analytics Data**. Find one starting with `pdfutils-` or `Simple Pdf Utils-` and attach its `.ips` file to the email.
