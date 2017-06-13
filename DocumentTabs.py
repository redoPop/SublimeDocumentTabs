import os
import sublime
import sublime_plugin
import subprocess
import threading

'''
---------------------------------------------------------------------
Globals
'''

NEXT_TAB_OSA = '''
tell application "System Events"
	tell first tab group of front window of application process "Sublime Text"
		set all_tabs to radio buttons
		set all_tabs_count to number of items in all_tabs

		set rightmost_tab_index to 0
		set rightmost_tab_left to 0

		# Find the index of the rightmost tab
		repeat with current_tab_index from 1 to all_tabs_count
			set current_tab_position to position of radio button current_tab_index
			set current_tab_left to item 1 of current_tab_position

			if current_tab_left > rightmost_tab_left then
				set rightmost_tab_index to current_tab_index
				set rightmost_tab_left to current_tab_left
			end if
		end repeat

		# If rightmost tab is currently selected, target the first tab
		# Otherwise, target the next-frontmost tab
		if rightmost_tab_index is all_tabs_count then
			set target_tab_index to 1
		else
			set target_tab_index to all_tabs_count - 1
		end if

		# Select the targeted tab
		click radio button target_tab_index
	end tell
end tell
'''

PREV_TAB_OSA = '''
tell application "System Events"
	tell first tab group of front window of application process "Sublime Text"
		set all_tabs to radio buttons
		set all_tabs_count to number of items in all_tabs

		set rightmost_tab_index to 0
		set rightmost_tab_left to 0

		# Find the index of the rightmost tab
		repeat with current_tab_index from 1 to all_tabs_count
			set current_tab_position to position of radio button current_tab_index
			set current_tab_left to item 1 of current_tab_position

			if current_tab_left > rightmost_tab_left then
				set rightmost_tab_index to current_tab_index
				set rightmost_tab_left to current_tab_left
			end if
		end repeat

		set target_tab_index to rightmost_tab_index - 1
		if target_tab_index < 1 then set target_tab_index to 1

		# Select the targeted tab
		click radio button target_tab_index
	end tell
end tell
'''

PACKAGE_DIR = os.path.splitext(os.path.basename(os.path.dirname(__file__)))[0]

'''
---------------------------------------------------------------------
Helpers
'''

def run_osa(script):
	p = subprocess.Popen('/usr/bin/osascript', stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	script = script.encode('utf8')
	out = p.communicate(script)

'''
---------------------------------------------------------------------
Commands
'''

# Activate the next document tab
class DocumentTabsNextCommand(sublime_plugin.WindowCommand):
	def run(self):
		t = threading.Thread(target=run_osa, args=(NEXT_TAB_OSA,))
		t.daemon = True
		t.start()

# Activate the previous document tab
class DocumentTabsPrevCommand(sublime_plugin.WindowCommand):
	def run(self):
		t = threading.Thread(target=run_osa, args=(PREV_TAB_OSA,))
		t.daemon = True
		t.start()

# Open a file relative to the Document Tabs package directory
class DocumentTabsOpenFile(sublime_plugin.ApplicationCommand):
	def run(self, **args):
		args['file'] = '${packages}/' + PACKAGE_DIR + '/' + args.get('file')
		sublime.active_window().run_command('open_file', args)
