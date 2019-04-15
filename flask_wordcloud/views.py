from flask_wordcloud import *
from flask_wordcloud.settings import *
import os
from flask import Flask, redirect, render_template , request, url_for, send_file
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import time

UPLOAD_FOLDER = './media'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

image_size = {'1024×576':"10.24,5.76", "1280×720(HD)":"12.80,7.20", "1366×768":"13.66,7.68",
"1920×1080(FHD)":"19.20,10.80"}

def home_view():
    if request.method == 'POST':
        text = (request.form.get('file')).title()
        font_details = request.form.get('font_details')
        bg_color = request.form.get('background_color')
        try:
            height = (request.form.get("custom_height"))
            width = (request.form.get("custom_width"))
            height = float(height) / 100
            width = float(width) / 100

        except:
            fig_details = request.form.get('image_size')
            print(fig_details)
            size_details = (image_size.get(fig_details))
            size_details = size_details.split(',')
            height = float(size_details[0])
            width = float(size_details[1])

        fontPath ='./static/fonts/{}.ttf'.format(font_details)

        data = WordCloud(font_path = fontPath, background_color = "{}".format(bg_color), width=1600, height=800).generate(text)
        plt.figure( figsize = (height, width), facecolor='w', edgecolor='k' )
        plt.axis('off') #for off coord
        plt.tight_layout(pad=0)
        plt.imshow(data)
        name = str(time.time()).split('.')
        final_name = font_details+name[0]
        print(final_name)
        plt.savefig("./media/"+final_name)

        absolute_path = "../media/"+final_name+".png"

        return send_file(absolute_path, as_attachment=True)

    return render_template('wordcloud.html')

