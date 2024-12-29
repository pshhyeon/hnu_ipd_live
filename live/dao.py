import pymysql

class DaoLive:
    def __init__(self):
        self.con = pymysql.connect(
                                host='localhost', 
                                port=3306,
                                user='root', 
                                password='root',
                                db='live_cpted', 
                                charset='utf8')
                               
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)
        
    # user number 조회
    def selectUserNum(self,u_id,u_password):
        sql = f"""
            SELECT 
                user_num
            FROM user_info
            where
                user_id = '{u_id}' and user_pwd = '{u_password}'
        """
        self.cur.execute(sql)
        vo = self.cur.fetchone()
        return vo
    
    def selectNewPwdId(self):
        # PWD_ID 값 계산
        select_sql = "SELECT max(PWD_ID) + 1 NEW_PWD_ID FROM pwd_info"
        self.cur.execute(select_sql)
        result = self.cur.fetchone()  # 결과 가져오기
        # print("selectNewPwdId 결과:", result)  # 디버깅 출력
        return result

    # 비밀번호 저장
    def savePassword(self, hashed_password, new_pwd_id, user_num, room_no):
        # INSERT 실행
        insert_sql = """
            INSERT INTO 
                pwd_info (PWD_ID, USER_NUM, PWD, REG_YMD, USE_ONCE_YN, ROOM_NO)
            VALUES
                (%s, %s, %s, SYSDATE(), %s, %s)
        """

        # sql에 직접 값을 넣으면 sql 주입 공격 방지를위해서 execute에 파라미터 바인딩을 한다
        cnt = self.cur.execute(insert_sql, (new_pwd_id, user_num, hashed_password, 'y', room_no))
        self.con.commit()  # 변경 사항 저장
        return cnt
    
    # room_no 비밀번호 리스트 조회
    def selectPwdList(self, room_no):
        sql = """
            SELECT 
                PWD_ID, USER_NUM, PWD, REG_YMD,DEL_DT, USE_ONCE_YN, ROOM_NO 
            FROM 
                pwd_info 
            WHERE 
            ROOM_NO = %s
        """
        self.cur.execute(sql, (room_no,))
        list = self.cur.fetchall()
        return list
    
    # 비밀번호 파기
    def updateDelDate(self, pwd_id):
        sql = """
            UPDATE pwd_info
            SET DEL_DT = SYSDATE()
            WHERE PWD_ID = %s
        """
        
        cnt = self.cur.execute(sql, (pwd_id,))
        self.con.commit()
        return cnt
        

    
    # 예제입니다.
    def selectList(self):
        sql = """
            SELECT 
                e_id,e_name,gen,addr
            FROM emp
        """
        self.cur.execute(sql)
        
        list = self.cur.fetchall()
        return list

    def selectOne(self,e_id):
        sql = f"""
            SELECT 
                e_id,e_name,gen,addr
            FROM emp
            where
                e_id = '{e_id}'
        """
        self.cur.execute(sql)
        
        vo = self.cur.fetchone()
        return vo
    
    def insert(self,e_id,e_name,gen,addr):
        sql = f"""
            INSERT INTO emp 
                (e_id,e_name,gen,addr) 
            VALUES 
                ('{e_id}','{e_name}','{gen}','{addr}')
        """
        
        cnt = self.cur.execute(sql)
        self.con.commit()
        return cnt
    
    def update(self,e_id,e_name,gen,addr):
        sql = f"""
            update emp
            set 
                e_name = '{e_name}',
                gen = '{gen}',
                addr = '{addr}'
            where
                e_id = '{e_id}'
        """
        
        cnt = self.cur.execute(sql)
        self.con.commit()
        return cnt
    
    def delete(self,e_id):
        sql = f"""
            delete from emp
            where
                e_id = '{e_id}'
        """
        
        cnt = self.cur.execute(sql)
        self.con.commit()
        return cnt
    
    
    def __del__(self):
        self.cur.close()
        self.con.close()
      
      
























