from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def get_pic():

    if request.args.get("course") is not None:
        course = request.args.get("course")
        name = request.args.get("name")
        id = request.args.get("id")
        company = request.args.get("company")
    else:
        course = request.form.get('course')
        name = request.form.get('name')
        id = request.form.get('id')
        company = request.form.get('company')


    html =  (
            "\n"
            "<!DOCTYPE html\n"
            "	PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n"
            "<html xmlns=\"https://www.w3.org/1999/xhtml\">\n"
            "\n"
            "<head>\n"
            "	<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />\n"
            "	<meta http-equiv=\"X-UA-Compatible\" content=\"IE=7\" />\n"
            "	<title>“青年大学习”第十三季</title>\n"
            "	<meta content=\"width=device-width, initial-scale=1\" name=\"viewport\" />\n"
            "	<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\" />\n"
            "	<meta name=\"format-detection\" content=\"telephone=no\">\n"
            "\n"
            "	<script type=\"text/javascript\" src=\"https://res.wx.qq.com/open/js/jweixin-1.0.0.js\"></script>\n"
            "	<script type=\"text/javascript\" src=\"https://ajax.aspnetcdn.com/ajax/jquery/jquery-1.9.0.min.js\"></script>\n"
            "\n"
            "	<script>\n"
            "		if (!window.jQuery)\n"
            "			document.write('<script type=\"text/javascript\" src=\"http://cdnsite.fjg360.cn/jquery-1.9.1.min.js\"><' + '/script>');\n"
            "		//http://cdnsite.fjg360.cn/jquery-1.9.1.min.js\n"
            "\n"
            "		if (navigator.userAgent.toLowerCase().match(/huawei/i) == \"huawei\") {\n"
            "			//转化rem单位\n"
            "			(function (doc, win) {\n"
            "				var docEl = doc.documentElement,\n"
            "					resizeEvt = 'orientationchange' in window ? 'orientationchange' : 'resize',\n"
            "					recalc = function () {\n"
            "						var clientWidth = docEl.clientWidth;\n"
            "						if (!clientWidth) return;\n"
            "						if (clientWidth >= 750) {\n"
            "							docEl.style.fontSize = '100px';\n"
            "						} else {\n"
            "							docEl.style.fontSize = 100 * (clientWidth / 1500) + 'px';\n"
            "						}\n"
            "						var html = document.getElementsByTagName('html')[0]\n"
            "						var settingFs = parseInt(100 * (clientWidth / 1500))\n"
            "						var settedFs = settingFs\n"
            "						var whileCount = 0\n"
            "						while (true) {\n"
            "							var realFs = parseInt(window.getComputedStyle(html).fontSize)\n"
            "							var delta = realFs - settedFs\n"
            "							// 不相等\n"
            "							if (Math.abs(delta) >= 1) {\n"
            "								if (delta > 0) {\n"
            "									settingFs--\n"
            "								} else {\n"
            "									settingFs++\n"
            "								}\n"
            "								html.setAttribute('style', 'font-size:' + settingFs + 'px!important')\n"
            "							} else {\n"
            "								break\n"
            "							}\n"
            "							if (whileCount++ > 100) {\n"
            "								break\n"
            "							}\n"
            "						}\n"
            "					};\n"
            "				if (!doc.addEventListener) return;\n"
            "				win.addEventListener(resizeEvt, recalc, false);\n"
            "				doc.addEventListener('DOMContentLoaded', recalc, false);\n"
            "			})(document, window);\n"
            "		} else {\n"
            "			(function (doc, win) {\n"
            "				var docEl = doc.documentElement,\n"
            "					resizeEvt = 'orientationchange' in window ? 'orientationchange' : 'resize',\n"
            "					recalc = function () {\n"
            "						var clientWidth = docEl.clientWidth;\n"
            "						if (!clientWidth) return;\n"
            "						if (clientWidth >= 1500) {\n"
            "							docEl.style.fontSize = '100px';\n"
            "						} else {\n"
            "							docEl.style.fontSize = 100 * (clientWidth / 1500) + 'px';\n"
            "							var div = document.createElement('div');\n"
            "							div.style.width = '1.4rem';\n"
            "							div.style.height = '0';\n"
            "							document.body.appendChild(div);\n"
            "							var ideal = 140 * clientWidth / 1500;\n"
            "							var rmd = (div.clientWidth / ideal);\n"
            "							if (rmd > 1.2 || rmd < 0.8) {\n"
            "								docEl.style.fontSize = 100 * (clientWidth / 1500) / rmd + 'px';\n"
            "							}\n"
            "							document.body.removeChild(div);\n"
            "						};\n"
            "					};\n"
            "				if (!doc.addEventListener) return;\n"
            "				win.addEventListener(resizeEvt, recalc, false);\n"
            "				doc.addEventListener('DOMContentLoaded', recalc, false);\n"
            "			})(document, window);\n"
            "		}\n"
            "\n"
            "	</script>\n"
            "	<script>\n"
            "\n"
            "\n"
            "		$(function () {\n"
            "			var size = $(document).width() / 1500;\n"
            "			var screen_height = 936 * size * 2;\n"
            "			var height = $(document).height();\n"
            "			if (screen_height > $(document).height()) {\n"
            "				//$('#con').css('height',screen_height);\n"
            "			}\n"
            "			else {\n"
            "				//$('#con').css('height',$(document).height());\n"
            "			}\n"
            "\n"
            "			//$('#con').css('height',$(document).height());\n"
            "			$('#con_bind').css('height', $(document).height());\n"
            "			$('#cover2').css('height', $(document).height());\n"
            "			$('#con').css('height', $(document).height());\n"
            "			$('#con_first').css('height', $(document).height());\n"
            "			//$('#con').css({'-webkit-transform':'scale(1,' + height/screen_height + ')'});\n"
            "			$('#peoples').css('top', 207 * size + 'px');\n"
            "			$('#peoples').css('font-size', 20 * size + 'px');\n"
            "			$('#date').css('top', 515 * size + 'px');\n"
            "			$('#rule1').css('top', 400 * size + 'px');\n"
            "			$('#rule1').css('font-size', 22 * size + 'px');\n"
            "			$('#rule1').css('line-height', 40 * size + 'px');\n"
            "			$('#dialog>div').css('font-size', 22 * size + 'px');\n"
            "			$('#dialog>div').css('line-height', 38 * size + 'px');\n"
            "			$('#rule2').css('top', 794 * size + 'px');\n"
            "			$('#dialog').css('top', 420 * size + 'px');\n"
            "			$('#dialog').css('height', 376 * size + 'px');\n"
            "			$('#dialog2').css('top', 380 * size + 'px');\n"
            "			$('#dialog2').css('height', 376 * size + 'px');\n"
            "			$('#dialog2>img').css('height', 476 * size * 1.0 + 'px');\n"
            "			$('#btn').css('top', 805 * size + 'px');\n"
            "			$('#btn').css('height', 353 * size + 'px');\n"
            "\n"
            "		})\n"
            "	</script>\n"
            "	<style>\n"
            "		#con {\n"
            "			-webkit-transform-origin: top left;\n"
            "			-moz-transform-origin: top left;\n"
            "			-o-transform-origin: top left;\n"
            "			transform-origin: top left;\n"
            "		}\n"
            "\n"
            "		body,\n"
            "		html {\n"
            "			overflow: hidden;\n"
            "		}\n"
            "\n"
            "		.btn4 {\n"
            "			width: 11.71rem;\n"
            "			height: 1.77rem;\n"
            "			float: left;\n"
            "			position: absolute;\n"
            "			left: 1.74rem;\n"
            "			top: 14.82rem;\n"
            "		}\n"
            "\n"
            "		.clear {\n"
            "			clear: both\n"
            "		}\n"
            "\n"
            "		.main {\n"
            "			width: 12.1rem;\n"
            "			height: 7.23rem;\n"
            "			float: left;\n"
            "			position: absolute;\n"
            "			left: 1.44rem;\n"
            "			top: 13rem;\n"
            "		}\n"
            "\n"
            "		.main_title {\n"
            "			width: 11.33rem;\n"
            "			height: 0.98rem;\n"
            "			float: left;\n"
            "			margin-left: 0.79rem;\n"
            "			margin-top: 0.61rem;\n"
            "			color: #333333;\n"
            "			font-size: 0.6rem;\n"
            "			line-height: 0.97rem;\n"
            "			font-weight: bold;\n"
            "		}\n"
            "\n"
            "		.main_forum {\n"
            "			width: 11.27rem;\n"
            "			height: 1.08rem;\n"
            "			float: left;\n"
            "			margin-left: 0.79rem;\n"
            "			margin-top: 0.25rem;\n"
            "			color: #333333;\n"
            "			font-size: 0.6rem;\n"
            "			line-height: 0.97rem;\n"
            "			font-weight: bold;\n"
            "		}\n"
            "\n"
            "		.main_close {\n"
            "			width: 11.31rem;\n"
            "			height: 0.98rem;\n"
            "			float: left;\n"
            "			margin-left: 0.79rem;\n"
            "			margin-top: 0.19rem;\n"
            "			color: #333333;\n"
            "			font-size: 0.6rem;\n"
            "			line-height: 0.97rem;\n"
            "			font-weight: bold;\n"
            "		}\n"
            "\n"
            "		.main_thumbnail {\n"
            "			width: 11.34rem;\n"
            "			height: 2.69rem;\n"
            "			float: left;\n"
            "			margin-left: 0.76rem;\n"
            "			margin-top: 0.3rem;\n"
            "			color: #333333;\n"
            "			font-size: 0.6rem;\n"
            "			line-height: 0.9rem;\n"
            "			font-weight: bold;\n"
            "		}\n"
            "\n"
            "		.forum {\n"
            "			width: 3.63rem;\n"
            "			height: 1.43rem;\n"
            "			float: left;\n"
            "			position: absolute;\n"
            "			left: 1.93rem;\n"
            "			top: 21.45rem;\n"
            "		}\n"
            "\n"
            "		.forum2 {\n"
            "			width: 3.63rem;\n"
            "			height: 1.43rem;\n"
            "			float: left;\n"
            "			position: absolute;\n"
            "			left: 9.2rem;\n"
            "			top: 21.45rem;\n"
            "		}\n"
            "\n"
            "		.aside {\n"
            "			width: 3.66rem;\n"
            "			height: 1.41rem;\n"
            "			float: left;\n"
            "			margin-left: 9.34rem;\n"
            "			margin-top: 21.46rem;\n"
            "		}\n"
            "	</style>\n"
            "</head>\n"
            "\n"
            "<body style='margin: 0px; font-family: \"微软雅黑\"; background-color:#848fa4;'>\n"
            "\n"
            "	<div id=\"center_con\">\n"
            "		<div id='con_bind'\n"
            "			style='display:none;width: 100%;  background: url(http://cdnsite.fjg360.cn/18da/back4.png?v=3) no-repeat; background-size: 100%; background-color: #848fa3; overflow: hidden; position: absolute;'>\n"
            "\n"
            "			<div style=\"background:white;border-radius:0.5rem;font-size:0.62rem;line-height:1.35rem;text-align:center;color:#ED502E;font-weight:bold;\"\n"
            "				onclick=\"edit_next()\" id=\"forum\" class=\"forum\">\n"
            "				修改信息\n"
            "			</div>\n"
            "\n"
            "			<div style=\"background:white;border-radius:0.5rem;font-size:0.62rem;line-height:1.35rem;text-align:center;color:#ED502E;font-weight:bold;\"\n"
            "				onclick=\"goNext2()\" id=\"forum2\" class=\"forum2\">\n"
            "				确 &nbsp; 定\n"
            "			</div>\n"
            "\n"
            "			<div id=\"main\" class=\"main\">\n"
            "\n"
            "				<div id=\"main_title\" class=\"main_title\">\n"
            "					当前课程：<span id=\"now_lesson\">"+ str(course) +"</span></div>\n"
                                                                              "\n"
                                                                              "				<div id=\"main_forum\" class=\"main_forum\">\n"
                                                                              "					您的姓名：<span id=\"now_name\">"+ str(name) +"</span></div>\n"
                                                                                                                                            "\n"
                                                                                                                                            "				<div id=\"main_close\" class=\"main_close\">\n"
                                                                                                                                            "					用户编号：<span id=\"now_id\">"+ str(id) +"</span></div>\n"
                                                                                                                                                                                                      "\n"
                                                                                                                                                                                                      "				<div id=\"main_thumbnail\" class=\"main_thumbnail\">\n"
                                                                                                                                                                                                      "					所属单位：<span id=\"now_company\">"+ str(company) +"</span></div>\n"
                                                                                                                                                                                                                                                                          "			</div>\n"
                                                                                                                                                                                                                                                                          "		</div>\n"
                                                                                                                                                                                                                                                                          "\n"
                                                                                                                                                                                                                                                                          "		<script>\n"
                                                                                                                                                                                                                                                                          "			$('#con_bind').show();\n"
                                                                                                                                                                                                                                                                          "			$('#con_first').hide();\n"
                                                                                                                                                                                                                                                                          "		</script>\n"
                                                                                                                                                                                                                                                                          "</body>\n"
                                                                                                                                                                                                                                                                          "\n"
                                                                                                                                                                                                                                                                          "</html>\n"
                                                                                                                                                                                                                                                                          "            ")

    return html

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)