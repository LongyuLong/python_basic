from flask import Flask, render_template
from flask import request, redirect, url_for, flash
# flash: 임시 메세지 출력용 (내부적으로 세션에 저장해둠 - secret_key 필수), 세션을 import해서 쓰지 않더라도..?
import pymysql
import os
from flask import get_flashed_messages      # 저장해둔 메세지를 꺼내는 함수
# flash("에러~") -> 메세지를 세션에 잠시 저장 후 get_flashed_messages() 하면 메세지를 읽음, 일회용

app = Flask(__name__)
app.secret_key = "abcdef123456"             # session/flash를 위한 쿠키 서명용 비밀 key

# MariaDB 연결 정보
DB_HOST = os.getenv("DB_HOST","127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT","3306"))
DB_USER = os.getenv("DB_USER","root")
DB_PASSWORD = os.getenv("DB_PASSWORD","123")
DB_NAME = os.getenv("DB_NAME","test")

def get_conn():
    return pymysql.connect(
        host = DB_HOST,
        port = DB_PORT,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB_NAME,
        charset = "utf8mb4",        # utf8mb4: 전세계 문자 + 이모지 처리 가능
        cursorclass = pymysql.cursors.DictCursor, 
        # DictCursor: select 결과를 'dict type' 형태로 받게해줌
        # {'code':1,'sang':'마우스', ...} -> row['code'], row['sang'] ..
        autocommit=False
    )

@app.get("/")
def root():
    return redirect(url_for("show_list"))

@app.get("/show/")
def show_list():
    conn = get_conn()           # DB와 연결
    try:                        # 외부와 연결할 때는 try를 쓰는게 좋다
        with conn.cursor() as cur:
            cur.execute("select code, sang,su,dan from sangdata order by code")
            rows = cur.fetchall()
        messages = list(get_flashed_messages())
        return render_template("list.html", rows=rows, messages=messages)
    # except pymysql.err.IntegrityError as e:
    #  ...  와 같은 세부적인 표현도 가능하다
    except Exception as e:
        pass
    finally:
        conn.close()            # DB와 연결 해제

@app.get("/add/")
def add_form():
    messages = list(get_flashed_messages())
    return render_template("form_add.html", messages=messages)      # 추가 폼 호출

@app.post("/add/")
def add_save():                 # 추가 처리는 여기서
    sang = (request.form.get("sang") or "").strip()
    su_raw = (request.form.get("su") or "").strip()                   # "23" 으로넘어옴. 
    dan_raw = (request.form.get("dan") or "").strip()                 # 네트워크를 통한 전송은 숫자도 문자열로 취급되므로
    if not sang or not su_raw.isdigit() or not dan_raw.isdigit():   # isdigit
        flash("sang은 필수, su/dan은 숫자만 허용")
        return redirect(url_for("add_form"))

    su = int(su_raw)            # 연산 없이 추가이므로 숫자화 안해도 됨
    dan = int(dan_raw)
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            # code는 자동 증가 프로그래밍 하기
            cur.execute("select max(code) as max_code from sangdata")
            row = cur.fetchone()
            max_code = row["max_code"] if row else None     # 데이터가 아예 없을 수도 있으니까 else None까지
            next_code = (max_code + 1) if max_code is not None else 1   # SQL 문법이었나 조건문 순서가 좀 이상하네     
            # 추가하기
            cur.execute("insert into sangdata(code, sang, su, dan) values(%s, %s, %s, %s)", (next_code, sang, su, dan))
        conn.commit()
        return redirect(url_for("show_list"))

    except Exception as e:
        conn.rollback()
        flash(f"저장 실패: {e}")
        return redirect(url_for("add_form"))

    finally:
        conn.close()

@app.get("/edit/<int:code>/")
def edit_form(code:int):            # 수정 폼 호출
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("select * from sangdata where code=%s", (code,))    #튜플이어야하는 이유도 다시 복습
            row = cur.fetchone()
            if not row:
                flash("해당 자료가 없습니다.")
                return redirect(url_for("show_list"))
            messages = list(get_flashed_messages())
            return render_template("form_edit.html", row=row, messages=messages)

    finally:
        conn.close()

@app.post("/edit/<int:code>/")
def edit_save(code:int):
    sang = (request.form.get("sang") or "").strip()
    su_raw = (request.form.get("su") or "").strip()                   
    dan_raw = (request.form.get("dan") or "").strip()                 
    if not sang or not su_raw.isdigit() or not dan_raw.isdigit():   
        flash("sang은 필수, su/dan은 숫자만 허용")
        return redirect(url_for("edit_form",code=code))
    su = int(su_raw)            # 연산 없이 추가이므로 숫자화 안해도 됨
    dan = int(dan_raw)
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            # 수정하기
            cur.execute("update sangdata set sang=%s, su=%s, dan=%s where code=%s", (sang, su, dan, code))
        conn.commit()
        return redirect(url_for("show_list"))

    except Exception as e:
        conn.rollback()
        flash(f"수정 실패: {e}")
        return redirect(url_for("edit_form",code=code))

    finally:
        conn.close()

@app.post("/delete/<int:code>/")
def delete_row(code:int):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            # 삭제하기
            cur.execute("delete from sangdata where code=%s", (code,))
        conn.commit()
        return redirect(url_for("show_list"))

    except Exception as e:
        conn.rollback()
        flash(f"삭제 실패: {e}")
        return redirect(url_for("show_list"))
    finally:
        conn.close()

if __name__=="__main__":
    app.run(debug=True)

