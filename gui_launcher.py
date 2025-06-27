import sys, os, subprocess, signal, shutil
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QMessageBox

HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
BACKUP_PATH = r"C:\Windows\System32\drivers\etc\hosts.bak"

class ServerGui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("로컬 서버 컨트롤러")
        self.setGeometry(300, 200, 400, 350)

        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText("포트 (예: 8000)")
        self.domain_input = QLineEdit()
        self.domain_input.setPlaceholderText("도메인 (예: test.com, default: localhost)")

        self.run_btn = QPushButton("실행")
        self.stop_btn = QPushButton("중단")
        self.run_btn.clicked.connect(self.start_all)
        self.stop_btn.clicked.connect(self.stop_all)

        self.status_label = QLabel("서버가 꺼져 있습니다.")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("포트"))
        layout.addWidget(self.port_input)
        layout.addWidget(QLabel("도메인"))
        layout.addWidget(self.domain_input)
        layout.addWidget(self.status_label)
        btns = QHBoxLayout()
        btns.addWidget(self.run_btn)
        btns.addWidget(self.stop_btn)
        layout.addLayout(btns)
        self.setLayout(layout)

        self.server_proc = None
        self.redirected_domain = ""
        self.server_port = ""

    def start_all(self):
        domain = self.domain_input.text().strip() or "localhost"
        port = self.port_input.text().strip() or "8000"
        self.redirected_domain = domain
        self.server_port = port

        if not port.isdigit():
            QMessageBox.warning(self, "오류", "포트는 숫자만 입력해야 합니다.")
            return

        if not self.backup_hosts():
            QMessageBox.warning(self, "오류", "hosts 파일 백업 실패(관리자 권한 필요)")
            return

        if not self.edit_hosts(domain):
            QMessageBox.warning(self, "오류", "hosts 파일 편집 실패(관리자 권한 필요)")
            return

        self.server_proc = subprocess.Popen(
            [sys.executable, "app.py", port], # app.py로 서버 실행
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
        )
        self.status_label.setText(f"서버가 열렸습니다.\n({domain}:{port})로 접속하세요.")

    def stop_all(self):
        if self.server_proc:
            self.server_proc.terminate()
            self.server_proc = None
        self.restore_hosts()
        self.status_label.setText("서버가 중단되었습니다.\n hosts 파일도 원복되었습니다.")

    def backup_hosts(self):
        try:
            if not os.path.exists(BACKUP_PATH):
                shutil.copyfile(HOSTS_PATH, BACKUP_PATH)
            return True
        except Exception as e:
            print("hosts 백업 오류:", e)
            return False

    def edit_hosts(self, domain):
        try:
            with open(HOSTS_PATH, "r", encoding="utf-8") as f:
                lines = f.readlines()
            # 기존 도메인 라인 삭제
            lines = [line for line in lines if not (line.strip().startswith("127.0.0.1") and domain in line)]
            lines.append(f"127.0.0.1    {domain}\n")
            with open(HOSTS_PATH, "w", encoding="utf-8") as f:
                f.writelines(lines)
            return True
        except Exception as e:
            print("hosts 수정 오류:", e)
            return False

    def restore_hosts(self):
        try:
            if os.path.exists(BACKUP_PATH):
                shutil.copyfile(BACKUP_PATH, HOSTS_PATH)
                os.remove(BACKUP_PATH)
        except Exception as e:
            print("hosts 복구 오류:", e)

    def closeEvent(self, event):
        self.stop_all()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = ServerGui()
    gui.show()
    sys.exit(app.exec_())