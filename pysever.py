from ast import keyword
from inspect import get_annotations
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)
data = {
    "1": {"id": "1",
          "name": "Michael Jordan",
          "headshot":"https://cdn.nba.com/manage/2021/10/30_michael_jordan.jpg",
          "image": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Michael_Jordan_in_2014.jpg",
          "birthyear": "1963",
          "feature": "A LEGACY OF CULTURAL GAME-CHANGING.",
          "overview": "Michael Jeffrey Jordan (born February 17, 1963), also known by his initials MJ, is an American businessman and former professional basketball player. His biography on the official National Basketball Association (NBA) website states: 'By acclamation, Michael Jordan is the greatest basketball player of all time.' He was integral in popularizing the NBA around the world in the 1980s and 1990s, becoming a global cultural icon in the process. Jordan played 15 seasons in the NBA, winning six championships with the Chicago Bulls. He is the principal owner and chairman of the Charlotte Hornets of the NBA and of 23XI Racing in the NASCAR Cup Series.",
          "years": ["Chicago Bulls (1984-1993, 1995-1998)", "Washington Wizards (2001-2003)"],
          "position": "Guard",
          "points": "32292",
          "rebounds": "6672",
          "assists": "5633",
          "championships": [
              "1991", "1992", "1993", "1996", "1997", "1998"],
          "mvp": ["1988", "1991", "1992", "1996", "1998"],
          "fmvp": ["1991", "1992", "1993", "1996", "1997", "1998"],
          "allstar": "14",
          "allnba": "11", },

    "2": {"id": "2",
          "name": "LeBron James",
          "headshot":"https://cdn.nba.com/manage/2021/10/30_lebron_james.jpg",
          "image": "https://upload.wikimedia.org/wikipedia/commons/c/cf/LeBron_James_crop.jpg",
          "birthyear": "1984",
          "feature": "RARE COMBINATION OF SIZE, SKILL AND SAVVY.",
          "overview": "LeBron Raymone James Sr. (/lə'brɒn/; born December 30, 1984) is an American professional basketball player for the Los Angeles Lakers of the National Basketball Association (NBA). A contender for the moniker of best NBA player of all time, LeBron James appears to be the rare case of a player seemingly performing in his prime over the course of nearly 20 years. A four-time MVP, four-time NBA champion and four-time Finals MVP, James turns 37 in December, but has averaged at least 25 points in every season except his rookie year (2003-04), in which he won Rookie of the Year.",
          "years": ["Cleveland Cavaliers (2003-2010, 2014-2018)", "Miami Heat (2010-2014)", "Los Angeles Lakers (2018-2021)"],
          "position": "Forward",
          "points": "35385",
          "rebounds": "9751",
          "assists": "9696",
          "championships": ["2012", "2013", "2016", "2020"],
          "mvp": ["2009", "2010", "2012", "2013"],
          "fmvp": ["2012", "2013", "2016", "2020"],
          "allstar": "17",
          "allnba": "17"
          },
    "3": {"id": "3",
          "name": "Kareem Abdul-Jabbar",
          "headshot":"https://cdn.nba.com/manage/2021/10/30_kareem_abdul_jabbar.jpg",
          "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Kareem_Abdul-Jabbar_May_2014.jpg/1280px-Kareem_Abdul-Jabbar_May_2014.jpg",
          "birthyear": "1947",
          "feature": "GAME-CHANGING IMPACT ON AND OFF COURT.",
          "overview": "Kareem Abdul-Jabbar (born Ferdinand Lewis Alcindor Jr.; April 16, 1947) is an American former professional basketball player who played 20 seasons in the National Basketball Association (NBA) for the Milwaukee Bucks and the Los Angeles Lakers. During his career as a center, Abdul-Jabbar was a record six-time NBA Most Valuable Player (MVP), a record 19-time NBA All-Star, a 15-time All-NBA selection, and an 11-time NBA All-Defensive Team member. A member of six NBA championship teams as a player and two more as an assistant coach, Abdul-Jabbar twice was voted NBA Finals MVP. He was named to the league's 35th, 50th and 75th anniversary teams. NBA coach Pat Riley and players Isiah Thomas and Julius Erving called him the greatest basketball player of all time.",
          "years": ["Milwaukee Bucks (1969-1975)", "Los Angeles Lakers (1975-1989)"],
          "position": "Center",
          "points": "38387	",
          "rebounds": "17440",
          "assists": "5660",
          "championships": ["1971", "1980", "1982", "1985", "1987", "1988"],
          "mvp": ["1971", "1972", "1974", "1976", "1977", "1980"],
          "fmvp": ["1971", "1985"],
          "allstar": "19",
          "allnba": "15"
          },
    "4": {"id": "4",
          "name": "Bill Russell",
          "headshot":"https://cdn.nba.com/manage/2022/01/Bill-Russ-Archive-75-16x9-NEW.jpg?w=384&h=224",
          "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Bill_Russell_in_the_Green_Room.jpg/440px-Bill_Russell_in_the_Green_Room.jpg",
          "birthyear": "1934",
          "feature": "A LASTING LEGACY THAT BROKE BARRIERS.",
          "overview": "William Felton Russell (born February 12, 1934) is an American former professional basketball player who played as a center for the Boston Celtics of the National Basketball Association (NBA) from 1956 to 1969. A five-time NBA Most Valuable Player and a 12-time All-Star, he was the centerpiece of the Celtics dynasty that won eleven NBA championships during his 13-year career. Russell and Henri Richard of the National Hockey League are tied for the record of the most championships won by an athlete in a North American sports league. Russell led the San Francisco Dons to two consecutive NCAA championships in 1955 and 1956, and he captained the gold-medal winning U.S. national basketball team at the 1956 Summer Olympics.",
          "years": ["Boston Celtics (1956-1969)"],
          "position": "Center",
          "points": "14522",
          "rebounds": "21620",
          "assists": "4100",
          "championships": ["1957", "1959", "1960", "1961", "1962", "1963", "1964", "1965", "1966", "1968", "1969"],
          "mvp": ["1958", "1961", "1962", "1963", "1965"],
          "fmvp": [None],
          "allstar": "12",
          "allnba": "11"
          },
    "5": {"id": "5",
          "name": "Magic Johnson",
          "headshot":"https://cdn.nba.com/manage/2021/10/30_magic_johnson.jpg",
          "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Magic_Johnson_2014_%28cropped%29.jpg/440px-Magic_Johnson_2014_%28cropped%29.jpg",
          "birthyear": "1959",
          "feature": "PURE BRILLIANCE REVOLUTIONIZED THE GAME.",
          "overview": "Earvin “Magic” Johnson Jr. (born August 14, 1959) is an American former professional basketball player and former president of basketball operations of the Los Angeles Lakers of the National Basketball Association (NBA). Often regarded as the best point guard of all time, Johnson played 13 seasons for the Lakers and was honored as one of the 50 Greatest Players in NBA History in 1996. After winning championships in high school and college, Johnson was selected first overall in the 1979 NBA draft by the Lakers. He won a championship and an NBA Finals Most Valuable Player Award in his rookie season, and won four more championships with the Lakers during the 1980s. Johnson retired abruptly in 1991 after announcing that he had contracted HIV, but returned to play in the 1992 All-Star Game, winning the All-Star MVP Award. After protests from his fellow players, he retired again for four years, but returned in 1996, at age 36, to play 32 games for the Lakers before retiring for the third and final time.",
          "years": ["os Angeles Lakers (1979-1991, 1996)"],
          "position": "Guard",
          "points": "17707",
          "rebounds": "6559",
          "assists": "10141",
          "championships": ["1980", "1982", "1985", "1987", "1988"],
          "mvp": ["1987", "1989", "1990"],
          "fmvp": ["1980", "1982", "1987"],
          "allstar": "12",
          "allnba": "10"
          },
    "6": {"id": "6",
          "name": "Wilt Chamberlain",
          "headshot":"https://cdn.nba.com/manage/2021/10/30_wilt_chamberlain.jpg",
          "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Wilt_Chamberlain3.jpg/440px-Wilt_Chamberlain3.jpg",
          "birthyear": "1936",
          "feature": "A PHENOMENAL TALENT THAT DID IT ALL.",
          "overview": "Wilton Norman Chamberlain (/ˈtʃeɪmbərlɪn/; August 21, 1936 – October 12, 1999) was an American professional basketball player who played as a center, and is widely regarded as one of the greatest players in the sport's history. He played for the Philadelphia/San Francisco Warriors, the Philadelphia 76ers, and the Los Angeles Lakers of the National Basketball Association (NBA). He played for the University of Kansas and for the Harlem Globetrotters before playing in the NBA. Chamberlain stood 7 ft 1 in (2.16 m) tall.",
          "years": ["Philadelphia / San Francisco Warriors (1959-1965)", "Philadelphia 76ers (1965-1968)", "Los Angeles Lakers (1968-1973)"],
          "position": "Center",
          "points": "31419",
          "rebounds": "23924",
          "assists": "4643",
          "championships": ["1967", "1972"],
          "mvp": ["1960", "1966", "1967", "1968"],
          "fmvp": ["1972"],
          "allstar": "13",
          "allnba": "10"
          },
    "7": {"id": "7",
          "name": "Larry Bird",
          "headshot":"https://cdn.nba.com/manage/2021/10/30_larry_bird.jpg",
          "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Larrybird.jpg/440px-Larrybird.jpg",
          "birthyear": "1956",
          "feature": "EXPLOSIVE PLAYMAKING AND A DEADLY SHOT.",
          "overview": "Larry Joe Bird (born December 7, 1956) is an American former professional basketball player, coach and executive in the National Basketball Association (NBA). Nicknamed “the Hick from French Lick” and “Larry Legend,” Bird is widely regarded as one of the greatest basketball players of all time. Growing up in French Lick, Indiana, he was a local basketball phenom. Highly recruited, he initially signed to play for coach Bobby Knight of the Indiana Hoosiers, but dropped out after one month and returned to French Lick to attend a local community college. The next year he attended the smaller Indiana State University, playing ultimately for three years for the Sycamores. Drafted by the Boston Celtics with the sixth overall pick in the 1978 NBA draft after his second year at Indiana State, Bird elected to stay in college and play one more season. He then led his team to an undefeated regular season in 1978–1979. The season finished with a national championship game matchup against Michigan State, a team that featured Magic Johnson, beginning a career-long rivalry that the two shared for more than a decade.",
          "years": ["Boston Celtics (1979-1992)"],
          "position": "Forward",
          "points": "21791",
          "rebounds": "8974",
          "assists": "5695",
          "championships": ["1981", "1984", "1986"],
          "mvp": ["1984", "1985", "1986"],
          "fmvp": ["1984", "1986"],
          "allstar": "12",
          "allnba": "10"
          },
    "8": {"id": "8",
          "name": "Shaquille O'Neal",
          "headshot":"https://cdn.nba.com/manage/2021/10/30_shaq_oneal.jpg",
          "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Shaquille_O%27Neal_October_2017_%28cropped%29.jpg/440px-Shaquille_O%27Neal_October_2017_%28cropped%29.jpg",
          "birthyear": "1972",
          "feature": "THE ENTERTAINER WITH UNLIMITED TALENT.",
          "overview": "Shaquille Rashaun O'Neal (/ʃəˈkiːl/ shə-KEEL; born March 6, 1972), known commonly as “Shaq” (/ʃæk/ SHAK), is an American former professional basketball player who is a sports analyst on the television program Inside the NBA. O'Neal is regarded as one of the greatest basketball players and centers of all time. He is a 7 ft 1 in and 325 lb center who played for six teams over his 19-year career in the National Basketball Association (NBA) and is a four-time NBA champion.",
          "years": ["Orlando Magic (1992-1996)", "Los Angeles Lakers (1996-2004)", "Miami Heat (2004-2008)", "Phoenix Suns (2008-2009)", "Cleveland Cavaliers (2009-2010)", "Boston Celtics (2010-2011)"],
          "position": "Center",
          "points": "28596",
          "rebounds": "13099",
          "assists": "3026",
          "championships": ["2000", "2001", "2002", "2006"],
          "mvp": ["2000"],
          "fmvp": ["2000", "2001", "2002"],
          "allstar": "15",
          "allnba": "14"
          },
    "9": {"id": "9",
          "name": "Tim Duncan",
          "headshot":"https://cdn.nba.com/manage/2021/10/30_tim_duncan.jpg",
          "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Tim_Duncan.jpg/440px-Tim_Duncan.jpg",
          "birthyear": "1976",
          "feature": "IMPECCABLE DEFENSE AND ABILITY TO ADAPT.",
          "overview": "Timothy Theodore Duncan (born April 25, 1976)[1] is an American former professional basketball player and coach. Nicknamed “the Big Fundamental”, he is widely regarded as the greatest power forward of all time and one of the greatest players in NBA history.[2][3][4] He spent his entire 19-year playing career with the San Antonio Spurs. He was inducted into the Naismith Memorial Basketball Hall of Fame in 2020 and named to the NBA 75th Anniversary Team in 2021.",
          "years": ["San Antonio Spurs (1997-2016)"],
          "position": "Forward/Center",
          "points": "26496",
          "rebounds": "26496",
          "assists": "4225",
          "championships": ["1999", "2003", "2005", "2007", "2014"],
          "mvp": ["2002", "2003"],
          "fmvp": ["1999", "2003", "2005"],
          "allstar": "15",
          "allnba": "15"
          },
    "10": {"id": "10",
           "name": "Kobe Bryant",
           "headshot":"https://cdn.nba.com/manage/2021/10/30_kobe_bryant.jpg",
           "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kobe_Bryant_2014.jpg/440px-Kobe_Bryant_2014.jpg",
           "birthyear": "1978",
           "feature": "LEGACY OF UNWAVERED PASSION AND WORK ETHIC.",
           "overview": "Kobe Bean Bryant (/ˈkoʊbiː/ KOH-bee; August 23, 1978 – January 26, 2020) was an American professional basketball player. A shooting guard, he spent his entire 20-year career with the Los Angeles Lakers in the National Basketball Association (NBA). Widely regarded as one of the greatest basketball players of all time, Bryant won five NBA championships, was an 18-time All-Star, a 15-time member of the All-NBA Team, a 12-time member of the All-Defensive Team, the 2008 NBA Most Valuable Player (MVP), and a two-time NBA Finals MVP. Bryant also led the NBA in scoring twice, and ranks fourth in league all-time regular season and postseason scoring. He was posthumously voted into the Naismith Memorial Basketball Hall of Fame in 2020.",
           "years": ["Los Angeles Lakers (1996-2016)"],
           "position": "Guard",
           "points": "33643",
           "rebounds": "7047",
           "assists": "6306",
           "championships": ["2000", "2001", "2002", "2009", "2010"],
           "mvp": ["2008"],
           "fmvp": ["2009", "2010"],
           "allstar": "18",
           "allnba": "15"
           },


}

current_id = 10


def get_names():
    names = []
    for _, item in data.items():
        names.append(item["name"])
    return names


@app.route('/')
def homepage():
    keys_to_extract = ["1", "2", "10"]
    goats = {key: data[key] for key in keys_to_extract}
    print(goats)
    return render_template('homepage.html', goats=goats)


@app.route('/search/<keys>', methods=['GET', 'POST'])
def search(keys):

    global data

    search_result = []
    for _,item in data.items():
        if keys.lower() in item["name"].lower():
            item_found = item
            item_found["matched"]="name"
            
            item_found["position_st"] = item["name"].lower().find(keys.lower())
            item_found["position_en"] = item_found["position_st"] + len(keys)
            search_result.append(item_found)
        elif keys.lower() in item["position"].lower():
            item_found = item
            item_found["matched"] = "position"
            item_found["position_st"] = item["position"].lower().find(keys.lower())
            item_found["position_en"] = item_found["position_st"] + len(keys)
            search_result.append(item_found)    
                       

    print(search_result)

    return render_template('search_results.html', n_items=len(search_result), keys=keys, results=search_result)


@app.route('/view/<id>')
def view(id=None):
    global data
    one = data[id]
    return render_template('view.html', one=one)

@app.route('/edit/<id>')
def edit(id=None):
    global data
    one = data[id]
    return render_template('edit.html',one=one)

@app.route('/edit/edit_item', methods=['GET', 'POST'])
def edit_item():

    global data

    modified = request.get_json()
    id=modified["id"]
    print(modified)
    data[id].update(modified)
    
    return jsonify("success")






@app.route('/add')
def add():
    return render_template("create.html", names=get_names())

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():

    global data
    global current_id
    new_item = request.get_json()
    current_id += 1
    new_item["id"] = current_id
    txt = "{}"
    
    yearsorgin = new_item["years_origin"]
    career = txt.format(yearsorgin)
    history = career.split(",")    
    new_item["years"] = history

    champorgin = new_item["champ_origin"]
    champone = txt.format(champorgin)
    champs = champone.split(",")
    new_item["championships"] = champs

    mvporgin = new_item["mvp_origin"]
    mvpone = txt.format(mvporgin)
    mvps = mvpone.split(",")
    new_item["mvp"] = mvps

    fmvporgin = new_item["fmvp_origin"]
    fmvpone = txt.format(fmvporgin)
    fmvps = fmvpone.split(",")
    new_item["fmvp"] = fmvps

    data[txt.format(current_id)] = new_item
    print(data)

    return jsonify(url="view/"+str(new_item["id"]))


if __name__ == '__main__':
    app.run(debug=True)
