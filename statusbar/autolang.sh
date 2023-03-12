#!/bin/bash

# Default layout
DEFAULT_LAYOUT="us"

# Set the default layout initially
setxkbmap $DEFAULT_LAYOUT

# Monitor window focus
while true; do
    # Get the ID of the currently focused window
    current_window=$(xdotool getactivewindow)

    # Wait for 1 second
    # sleep 1

    # Check if the focused window has changed
    if [ "$(xdotool getactivewindow)" != "$current_window" ]; then
        # Get the current layout
        current_layout=$(setxkbmap -query | grep layout | awk '{print $2}')

        # Set the default layout if the layout is not the default
        if [ "$current_layout" != "$DEFAULT_LAYOUT" ]; then
            setxkbmap $DEFAULT_LAYOUT
            pkill -RTMIN+1 i3blocks
        fi
    fi
done


# #!/bin/bash

# # Set default keyboard layout
# default_layout="us"

# # Get the current keyboard layout
# current_layout=$(setxkbmap -query | grep layout | awk '{print $2}')

# # Export the current_layout variable as an environment variable
# export CURRENT_LAYOUT=$current_layout

# # Run an infinite loop to continuously check for mouse movement
# while true
# do
#     # Get the current position of the mouse
#     current_mouse_position=$(xdotool getmouselocation)

#     # If the mouse has moved and the current layout is not the default, set the keyboard layout to default
#     if [[ $current_mouse_position != $previous_mouse_position ]] && [[ $current_layout != $default_layout ]]
#     then
#         setxkbmap -layout $default_layout
#         current_layout=$default_layout
#         export CURRENT_LAYOUT=$current_layout
#     fi

#     # Store the current mouse position for the next iteration of the loop
#     previous_mouse_position=$current_mouse_position

#     # Get the current keyboard layout
#     current_layout=$(setxkbmap -query | grep layout | awk '{print $2}')
#     export CURRENT_LAYOUT=$current_layout

#     # Wait for 1 second before checking for mouse movement again
#     sleep 1
# done
