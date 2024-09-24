# # Fungsi menambahkan hasil prediksi ke spreadsheet
# def add_to_spreadsheet(self):
#     nama = self.lineEditNama.text()
#     nim = self.lineEditNim.text()
#     study_hours = self.spinBox_StudyHours.value()
#     previous_score = self.spinBox_PreviousExamScore.value()
#     prediction = self.labelPredictResult_2.text()
#     file_path = "result/predictions.xlsx"
#     if not os.path.exists("result"):
#         os.makedirs("result")
#     if not os.path.exists(file_path):
#         wb = openpyxl.Workbook()
#         sheet = wb.active
#         sheet.title = "Predictions"
#         sheet.append(["Name", "NIM", "Study Hours", "Previous Exam Score", "Prediction"])
#         wb.save(file_path)
#     wb = openpyxl.load_workbook(file_path)
#     sheet = wb.active
#     sheet.append([nama, nim, study_hours, previous_score, prediction])
#     wb.save(file_path)
#     msg_box = QMessageBox()
#     msg_box.setIcon(QMessageBox.Information)
#     msg_box.setWindowTitle("Success")
#     msg_box.setText("Prediction successfully added to the spreadsheet.")
#     msg_box.setStandardButtons(QMessageBox.Ok)
#     msg_box.exec_()
# # Fungsi Export spreadsheet
# def export_spreadsheet(self):
#     options = QFileDialog()
#     file_path, _ = QFileDialog.getSaveFileName(self,
#                                                "Save Spreadsheet",
#                                                "",
#                                                "Excel Files (*.xlsx);;All Files (*)",
#                                                options=options)
    
#     if file_path:
#         if not file_path.endswith(".xlsx"):
#             file_path += "*.xlsx"
#         original_file_path = "result/predictions.xlsx"
#         if os.path.exists(original_file_path):
#             wb = openpyxl.load_workbook(original_file_path)
#             wb.save(file_path)
            
#             msg_box = QMessageBox()
#             msg_box.setIcon(QMessageBox.Information)
#             msg_box.setWindowTitle("Export Success")
#             msg_box.setText(f"Spreadsheet has been successfully exported to:\n{file_path}")
#             msg_box.setStandardButtons(QMessageBox.Ok)
#             msg_box.exec_()
#         else:
#             msg_box = QMessageBox()
#             msg_box.setIcon(QMessageBox.Critical)
#             msg_box.setWindowTitle("Error")
#             msg_box.setText("Original spreadsheet file not found!")
#             msg_box.setStandardButtons(QMessageBox.Ok)
#             msg_box.exec_()