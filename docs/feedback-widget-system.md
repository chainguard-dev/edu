# Feedback Widget System Overview

This document provides an overview of the interactive feedback system implemented on Chainguard Academy, allowing users to provide feedback on content pages.

## What is the Feedback Widget?

The feedback widget is an interactive component that appears at the end of every article page, providing users with a simple "Was this helpful?" prompt with Yes/No options. User feedback is automatically collected and stored for content improvement analysis.

## How It Works

### User Experience Flow

1. **User visits an article page** → Widget appears after content, before related articles
2. **User clicks "Yes"** → Shows thumbs up emoji and "Thanks for the feedback!" message
3. **User clicks "No"** → Shows thumbs down emoji and reveals a text input field for detailed feedback
4. **User submits feedback** → Data is sent to Google Sheets for collection and analysis

### Technical Architecture

```
User Interaction → JavaScript → Google Apps Script → Google Sheets
```

- **Frontend**: Hugo-generated HTML with JavaScript for interactivity
- **Backend**: Google Apps Script web app for data processing  
- **Storage**: Google Sheets for feedback collection
- **Security**: Content Security Policy (CSP) configuration for external requests

## System Components

### Files Involved

**Frontend Templates:**
- `layouts/partials/feedback-widget.html` - Main widget HTML template
- `assets/scss/components/feedback-widget.scss` - Widget styling
- `assets/js/feedback-widget.js` - Interactive JavaScript functionality

**Integration Points:**
- `layouts/article/single.html` - Article page integration
- `layouts/article/single-semantic.html` - Semantic article page integration
- `layouts/wide/single.html` - Wide layout integration
- `layouts/partials/head/script-header.html` - CSP configuration
- `assets/scss/app.scss` - CSS imports

### Backend Services

**Google Apps Script Web App:**
- **Source Code**: "Feedback System Apps Script"
- **Function**: Processes feedback submissions and writes to Google Sheets
- **Deployment**: Web app deployment accessible to "Anyone" for public feedback collection

**Data Storage:**
- **Spreadsheet**: "Feedback Data Collection"
- **Format**: Structured data with timestamp, page info, feedback type, and user comments

The Feedback System Apps Script and Feedback Data Collection files are accessible to members of the Developer Enablement team.


## Features

### User Experience Features
- **Simple Interface**: Clear "Was this helpful?" question with Yes/No buttons
- **Positive Feedback**: One-click appreciation with visual confirmation
- **Negative Feedback**: Detailed feedback collection with text input
- **Character Limit**: 1000 character limit with real-time counter
- **Form Validation**: Required field validation and error handling
- **Responsive Design**: Works on mobile and desktop devices
- **Accessibility**: ARIA labels and keyboard navigation support
- **Theme Support**: Automatic dark mode compatibility

### Technical Features
- **Data Collection**: Automatic capture of page title, URL, feedback type, and text
- **Timestamp Recording**: Automatic date/time logging for each submission
- **CORS Handling**: Proper cross-origin request configuration
- **CSP Compliance**: Content Security Policy compatibility
- **Error Handling**: User-friendly error messages and graceful failures

## Data Structure

Each feedback submission creates a row in the Google Sheets with the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| **Timestamp** | Date and time of submission | `2025-01-16 10:30:45` |
| **Page Title** | Title of the page where feedback was given | `"Getting Started with Chainguard Images"` |
| **Page URL** | Full URL of the feedback page | `https://edu.chainguard.dev/chainguard/getting-started/` |
| **Feedback Type** | Type of feedback submitted | `"positive"` or `"negative"` |
| **Feedback Text** | User's detailed feedback | `"The examples were unclear"` (empty for positive feedback) |

## Security and Privacy

### Content Security Policy
The site's CSP has been updated to allow connections to:
- `https://script.google.com` (Apps Script endpoint)
- `https://script.googleusercontent.com` (Apps Script responses)

### Data Privacy
- **No personal information** is collected (no names, emails, IP addresses)
- **No tracking** beyond basic page context
- **Anonymous feedback** only - users cannot be identified
- **Public data** - all feedback is stored in accessible Google Sheets


Remember: The feedback widget helps improve content quality by providing direct user insights. Regular monitoring and response to feedback ensures the documentation continues to meet user needs effectively!
