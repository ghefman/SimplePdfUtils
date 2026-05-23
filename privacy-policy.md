# Privacy Policy — Simple Pdf Utils

_Last updated: 2026-05-23_

Simple Pdf Utils ("the app") is published by **DeltaWebOS**. This page explains what data the app collects and what it does with it.

## Short version

**Simple Pdf Utils does not collect, transmit, store, or share any data about you.**

The app processes the files you give it entirely on your device. The only network activity is a launch-time check to the app framework's update server (described in detail below), which sends anonymous framework metadata — no user data, no file contents, no identifiers tied to you or your Apple account.

## How the app handles your files

When you pick a PDF or image:

1. Your system component copies the file into the app's private cache.
2. The app reads the file locally to count pages, render thumbnails, measure size, or compress.
3. When you tap **Save**, the assembled PDF is written to the cache and handed to the iOS share sheet. You then choose where it goes.

At no point your files are uploaded anywhere by the app. iOS may sync the share-sheet destination (for example, if you choose iCloud Drive) — that's controlled by iOS and your settings, not by us.

## Permissions we request

**None**. The app **does not** request access to:

- The Photos library (the Files app handles photo imports through its own permission model).
- The microphone or camera.
- Location, contacts, calendars, or health data.
- Background processing or notifications.

## Analytics and tracking

We use none. The app contains no analytics SDK, no crash reporter, no advertising identifier, and no remote logging.

## App framework update check

Simple Pdf Utils is built with the Expo framework. On each app launch, the framework makes one HTTP request to Expo's update server (`u.expo.dev`) to check whether a bug-fix update is available for the app. This is the only network connection the app makes.

The request includes only anonymous framework metadata:

- A project identifier (the app's own identifier on Expo's build service).
- The runtime version the app declares.
- Your iOS version (so the server can serve a compatible update if one exists).
- A randomly-generated install identifier created locally by the framework, reset whenever you reinstall the app. This is **not** your Apple Identifier for Advertisers and is **not** linked to your Apple account, name, email, or any of your data.

The request does not include your name, email, location, the contents of any file you've worked with, or any identifier that can be tied back to you. The response is either "no update available" (the usual case) or, very rarely, the bytes of a new app bundle.

You can stop this check by enabling Airplane Mode — the rest of the app continues to work without a network connection.

## Third-party services

We use no third-party analytics, advertising, crash-reporting, or tracking services. The only third party the app communicates with is Expo, the open-source app framework, solely for the update check described above. Expo's privacy policy is at <https://expo.dev/privacy>.

## Children

The app does not knowingly collect any information from anyone, including children under 13. It collects nothing from any user.

## Changes to this policy

If we ever change how the app handles data, we will publish an updated policy here with a new "Last updated" date and bump the app version on the App Store.

## Contact

Questions or concerns:

- Email: **<ghefetz@gmail.com>**

---

## Verifying these claims yourself

Privacy promises are easy to make. You can verify ours without taking our word for it:

**Airplane Mode.** Enable Airplane Mode on your iPhone. Every feature of Simple Pdf Utils — picking files, reordering, removing, previewing, compressing, saving — works identically. The framework's update check fails silently (because the server is unreachable) and the rest of the app proceeds. If the app had been quietly uploading your files, Airplane Mode would break it.
