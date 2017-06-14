# Sublime Document Tabs

A **Sublime Text 3** plugin for macOS users that provides keyboard shortcuts for navigating macOS _document tabs_ within Sublime Text windows.

If you're unfamiliar, macOS document tabs can be used instead of windows when opening multiple Sublime Text projects:

![](https://github.com/redoPop/SublimeDocumentTabs/raw/master/doc-images/tabs.png)

(To switch from using multiple windows to using document tabs, navigate to the Dock section of your System Preferences and select "Prefer tabs when opening new documents: Always".)

The system-wide keyboard shortcuts for cycling through document tabs are `ctrl+tab` and `ctrl+shift+tab`, but these are overridden within Sublime Text. This plugin provides replacement Sublime Text key bindings for these shortcuts.

### Accessibility access

Because it uses AppleScript to control the active document tab, this plugin requires Sublime text to be given Accessibility access to control your computer:

1. In System Preferences, navigate to Security & Privacy ▸ Privacy ▸ Accessibility
2. Click the plus (+) button under the list of apps allowed to control your computer, and add Sublime Text

### Key bindings

Since its preferred key bindings override Sublime Text defaults, this plugin doesn't add any key bindings by default.

To add key bindings, go to **Preferences ▸ Package Settings ▸ Document Tabs ▸ Example Key Bindings** and copy the suggested key bindings to your personal key bindings file (Preferences ▸ Package Settings ▸ Document Tabs ▸ Key Bindings – User).

Remember that you can replace the suggested `ctrl+tab`/`ctrl+shift+tab` with whatever you prefer.

Personally, I prefer the consistency of the system-wide shortcut, so in my own keybindings I've moved Sublime Text's internal key bindings to `option+tab`/`option+shift+tab` and am using `ctrl+tab`/`ctrl+shift+tab` to cycle document tabs:

```
[
  { "keys": ["ctrl+tab"], "command": "document_tabs_next" },
  { "keys": ["ctrl+shift+tab"], "command": "document_tabs_prev" },

  { "keys": ["option+tab"], "command": "next_view_in_stack" },
  { "keys": ["option+shift+tab"], "command": "prev_view_in_stack" }
]
```

---

Thanks to lunixbochs on the Sublime Text forum for [the original suggestion.](https://forum.sublimetext.com/t/keyboard-shortcut-for-switching-between-fullscreen-sublime-projects-macos/25322/9)
