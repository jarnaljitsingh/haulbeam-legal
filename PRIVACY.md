# Haulbeam — Privacy Policy

**Effective date:** 26 May 2026
**Last updated:** 26 May 2026

This Privacy Policy explains how **Haulbeam** ("Haulbeam", "we", "us", "our") collects, uses, stores, shares and protects your personal information when you use the Haulbeam iOS app (the "App"). Haulbeam is a truck-navigation app for use in Australia. We handle personal information in line with the **Privacy Act 1988 (Cth)** and the **Australian Privacy Principles (APPs)**.

> **Provider:** Haulbeam, operated by an individual sole operator based in California, United States.
> **Contact:** support@jarnaljitsingh.com

By using the App, you agree to this Privacy Policy. If you do not agree, please do not use the App.

---

## 1. Who this applies to

The App is intended for **professional and heavy-vehicle drivers in Australia who are at least 18 years old**. It is not intended for children, and we do not knowingly collect personal information from anyone under 18.

---

## 2. Information we collect

We only collect information needed to plan truck-safe routes, run hands-free voice navigation, show and gather live road hazards, and operate your subscription. Specifically:

**a. Account & identity.** When you sign in with **Google** or **Apple**, we receive your **name, email address, profile photo URL**, and a unique user ID. We do not collect or store your Google or Apple password.

**b. Location & driving data.** With your permission, we collect your **precise GPS location** — including **in the background** while navigation is running — together with your heading and derived speed. Location is essential to plan and follow routes, show your position, warn you about restrictions and hazards, and alert you near weighbridges and safety stations.

**c. Voice & microphone.** When you use voice features, your microphone captures audio so the App can detect the "Hey Map" wake word and your spoken commands. **Speech is converted to text on your device** (using Apple's on-device speech recognition on supported hardware). **Only the resulting text** of your command — not the audio — is sent to our voice assistant for interpretation (see Section 4). Audio is not stored or transmitted off your device.

**d. Voice fingerprint (biometric) — stays on your device.** If you calibrate the wake word, the App creates a mathematical **voiceprint** of your voice and stores it **only on your device** to recognise when *you* say "Hey Map". This voiceprint is **never uploaded** to us or any third party, and the raw recordings used to create it are not retained.

**e. Truck profile.** The truck details you enter — name, height, width, length, weight, axle count, and whether you carry dangerous or refrigerated goods — used to calculate truck-safe routes. This is stored on your device and sent to our routing provider as needed (see Section 4).

**f. Destinations & searches.** Place names and addresses you type or speak, and a local history of your recent destinations.

**g. Reports & messages you create.** Hazard reports (type, an optional note, and the location), weighbridge "active/quiet" reports, and any route-chat messages. **These are shared with other drivers — see Section 5.**

**h. Device & diagnostic information.** A push-notification token, a device identifier (Apple's Identifier for Vendor) included in support reports, your app version, and on-device diagnostic logs. Logs stay on your device and are only sent to us if you choose to submit a problem report (see Section 4f); they may contain your location and the text of your voice commands.

**i. Subscription information.** Your subscription and free-trial status. Purchases are processed by **Apple** — we do not receive or store your payment-card details.

---

## 3. How we use your information

We use your information to:
- plan and display truck-safe routes and turn-by-turn navigation;
- show your live location, speed and upcoming restrictions;
- detect and act on your voice commands;
- show and collect live hazard and weighbridge reports from drivers;
- send push notifications about nearby heavy-vehicle safety stations;
- provide and enforce the free trial and subscription (including preventing repeat free trials on the same device);
- diagnose problems you report and keep the App secure and reliable.

We do **not** sell your personal information, and we do **not** use it for third-party advertising. Firebase Analytics and Ads are disabled in the App.

---

## 4. Who we share information with (service providers)

We use the following third parties to run the App. Each receives only the data needed for its function, and your data is transmitted over encrypted (HTTPS) connections.

**a. Google / Firebase** (authentication, database, push). Stores your driver profile, your reports, route-chat messages, and your push token + last location; handles sign-in and delivers push notifications. Firebase is operated by Google LLC.

**b. HERE Technologies** (mapping & routing). Receives your **route coordinates, truck dimensions, and place-search queries** to calculate truck-safe routes, power search and reverse-geocoding, and render the map.

**c. Cloudflare, Inc.** (voice command interpretation & trial protection). When you give a voice command, the **text transcript** plus limited trip context (your origin/destination coordinates, destination name, and truck profile name and dimensions) is sent to **Cloudflare Workers AI** to convert it into an in-app action. We also send an Apple **DeviceCheck** token to a Cloudflare service to enforce one free trial per device. *(Audio is never sent — only text.)*

**d. Apple** (sign-in, speech, payments, notifications, anti-abuse). Provides on-device speech recognition, Sign in with Apple, App Store subscription processing, push delivery, and the DeviceCheck device flag used to prevent trial abuse.

**e. OpenStreetMap / Overpass** (map data). Receives an area (bounding box) **around your route** to look up truck points of interest and road restrictions. This is location data, but not tied to your identity.

**f. Cloudinary** (support attachments). Only when you submit a "Report a problem", your screenshots and diagnostic logs are uploaded to Cloudinary so we can investigate.

Haulbeam is operated from the **United States (California)**, and the service providers above may store or process your information on servers **outside Australia** (including in the United States and other countries). This means your personal information is handled overseas. By using the App you consent to this overseas handling. We take reasonable steps to use reputable providers that protect your information.

We may also disclose information **if required by law** (for example, to comply with a court order or a lawful request from an authority).

---

## 5. Information visible to other drivers

Haulbeam is a community safety app. The following are **shared publicly with other Haulbeam drivers**:
- **Hazard reports** and **weighbridge status reports** you submit (their type, note, and location), and
- **Route-chat messages** you send (visible to drivers travelling a similar route).

Your **display name** may appear alongside reports and messages. **Please do not include personal, sensitive, or identifying information in notes or chat messages.** Do not submit false or misleading reports.

---

## 6. How long we keep information, and deletion

- **Your driver profile, push token and location record, and the hazard reports you submitted** are stored until you delete them or delete your account.
- **Crowd-sourced weighbridge reports** are automatically deleted after about 24 hours.
- **Problem/bug reports** you submit (and their attached screenshots and logs) are kept as a permanent support record and are **not** automatically deleted, so we can investigate issues and prevent abuse.
- **On-device data** (truck profile, settings, recent destinations, voiceprint, logs) remains on your device until you delete it or uninstall the App.

**Deleting your account.** In **Settings → Delete account**, after re-confirming your identity, we delete: your driver profile, your push/location record, the hazard reports you submitted, and your sign-in account. We also erase the on-device data listed above (truck profile, settings, recent destinations, voiceprint, and logs).

For transparency, the following are **not** removed by account deletion:
- the **device-level free-trial flag** (an anonymous Apple DeviceCheck bit), which we retain to prevent the same device from claiming repeated free trials;
- **problem/bug reports** you previously submitted (and their attachments), which are kept as described above;
- **route-chat messages** you previously sent; and
- your **App Store subscription**, which you must cancel separately through your Apple ID.

---

## 7. Your privacy rights

Under the Australian Privacy Principles you may:
- **access** the personal information we hold about you;
- **correct** information that is inaccurate or out of date (you can edit your profile and truck details in the App);
- **delete** your account and associated data (see Section 6);
- **withdraw permissions** at any time in iOS **Settings** (location, microphone, speech, notifications) — note that some features won't work without them;
- **complain** if you believe we've mishandled your information.

To make a request or complaint, contact us at **support@jarnaljitsingh.com**. We'll respond within a reasonable time. If you're not satisfied, you may contact the **Office of the Australian Information Commissioner (OAIC)** at [oaic.gov.au](https://www.oaic.gov.au).

---

## 8. Security

We use encrypted (HTTPS) connections for all network traffic, rely on Apple/Google sign-in (we never see your password), and restrict access to stored data through server security rules. Your voice fingerprint and diagnostic logs stay on your device unless you choose to share a report. No method of transmission or storage is completely secure, but we take reasonable steps to protect your information.

---

## 9. Children

The App is for users **18 and over** and is not directed at children. If you believe a child has provided us personal information, contact us and we will delete it.

---

## 10. Changes to this policy

We may update this Privacy Policy from time to time. We'll change the "Last updated" date above and, for significant changes, provide notice in the App. Continued use after an update means you accept the revised policy.

---

## 11. Contact us

**Haulbeam** — operated by a sole operator based in California, USA.
Privacy enquiries: support@jarnaljitsingh.com

---

*Haulbeam is a navigation aid, not a substitute for your own judgement. Always obey road signage and the law. See our Terms of Use for the full safety disclaimer.*
