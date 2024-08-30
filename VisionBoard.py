from pathlib import Path

def vboard_html(Output_file):
    vboard_content = ''' 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles.css">
        <title>Vision Board</title>
    </head>
    <body>
        <!-- Spotify Embed -->
        <iframe style="border-radius:12px; position:absolute; z-index:1;" 
                src="https://open.spotify.com/embed/playlist/1O965bMGakJQd8KDiChpDa?utm_source=generator" 
                frameborder="0" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
                loading="lazy">
        </iframe>

        <!-- SVG Image -->
        <img id="visionboard" src="Vision Board.svg" alt="Vision Board">
    </body>
    </html>
    '''
    
    path = Path(Output_file)
    path.write_text(vboard_content)

# Call the function to create the HTML file
vboard_html('hidden_elements.html')