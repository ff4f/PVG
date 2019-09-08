from odoo import api, models


class hr_appraisal_report(models.AbstractModel):
    _name = 'report.pvg_hr_appraisal.hr_appraisal_report'

    @api.model
    def _get_survey_data(self, survey_id, complete_servey_ids, goal):
        _survey_id = survey_id.id

        appraisal_data = {'survey_id': _survey_id, }
        pages = []
        total_max = 0
        for page_id in survey_id.page_ids:
            page = {'page_id': page_id.id, 'page_name': page_id.display_name}
            questions = []
            for _question in page_id.question_ids:
                answer_text = ''
                answer_free_text = ''
                answer_number = 0
                answer_date = ''
                max = 0
                answer_count = 0
                answer_score = 0
                matrix = []
                if _question.type == 'textbox' or _question.type == 'free_text' or _question.type == 'numerical_box' or _question.type == 'date':
                    for complete_survey in complete_servey_ids:
                        if complete_survey.survey_id.id == _survey_id:
                            answer_count += 1
                            for answer in complete_survey.user_input_line_ids:
                                if not answer.skipped and answer.question_id.id == _question.id:
                                    answer_text = answer.value_text
                                    answer_free_text = answer.value_free_text
                                    answer_number = answer.value_number
                                    answer_date = answer.value_date

                if _question.type == 'simple_choice' or _question.type == 'multiple_choice':
                    if _question.type == 'simple_choice':
                        for label in _question.labels_ids:
                            if max < label.quizz_mark:
                                max = label.quizz_mark
                    if _question.type == 'multiple_choice':
                        for label in _question.labels_ids:
                            max += label.quizz_mark
                    for complete_survey in complete_servey_ids:
                        if complete_survey.survey_id.id == _survey_id:
                            answer_count += 1
                            for answer in complete_survey.user_input_line_ids:
                                if not answer.skipped and answer.question_id.id == _question.id:
                                    answer_score += answer.quizz_mark
                    max = max * answer_count
                    total_max += max
                elif _question.type == 'matrix':
                    matrix = []
                    m_answers = []
                    m_questions = _question.labels_ids_2
                    for label in _question.labels_ids:
                        if max < label.quizz_mark:
                            max = label.quizz_mark
                    for complete_survey in complete_servey_ids:
                        if complete_survey.survey_id.id == _survey_id:
                            answer_count += 1
                            # m_answers.append(complete_survey.user_input_line_ids)
                            for answer in complete_survey.user_input_line_ids:
                                if answer.question_id.id == _question.id:
                                    m_answers.append(answer)
                    for m_question in m_questions:
                        answer_score = 0
                        for m_answer in m_answers:
                            if m_answer.value_suggested_row.id == m_question.id:
                                answer_score += m_answer.quizz_mark
                        matrix.append({'m_question': m_question.value, 'score': answer_score})
                    max = max * answer_count
                    for label in _question.labels_ids_2:
                        total_max += max
                question = {'question_id': _question.id, 'string': _question.question, 'max': max,
                            'score': answer_score, 'question_type': _question.type, 'matrix': matrix,
                            'answer_text': answer_text, 'answer_free_text': answer_free_text,
                            'answer_number': answer_number, 'answer_date': answer_date}
                questions.append(question)
            page['questions'] = questions
            pages.append(page)

        total_score = 0
        for complete_survey in complete_servey_ids:
            if complete_survey.survey_id.id == _survey_id:
                total_score += complete_survey.quizz_score
        total_score = (total_score / total_max) * 100
        gap = ((goal/total_max)*100) - total_score
        total_max = 100 - (total_score + gap)
        overall_page = {'page_id': 'overall_page', 'page_name': 'Over all', 'total_max': total_max,
                        'total_score': total_score, 'gap': gap}
        pages.append(overall_page)
        appraisal_data['pages'] = pages
        return appraisal_data

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = []
        for appraisal_id in docids:
            doc = self.env['hr.appraisal'].browse(appraisal_id)
            if doc.manager_appraisal and doc.manager_survey_id:
                doc.manager_appraisal_data = self._get_survey_data(doc.manager_survey_id, doc.survey_completed_ids, doc.manager_survey_goal)

            docs.append(doc)

            docargs = {
                'doc_ids': docids,
                'doc_model': 'hr.appraisal',
                'docs': docs,
            }
            return docargs
