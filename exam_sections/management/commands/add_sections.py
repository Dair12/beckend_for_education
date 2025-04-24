from django.core.management.base import BaseCommand
from exam_sections.models import Section

class Command(BaseCommand):
    help = 'Add predefined sections to the database'

    def handle(self, *args, **kwargs):
        # List of sections to add
        sections = [
            # ОРТ - экзаменационные предметы
            {"exam": "Общереспубликанское тестирование", "subject": "Математика", "section": "Общий раздел", "exam_code": "ОРТ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 180},
            {"exam": "Общереспубликанское тестирование", "subject": "Аналогии и дополнения", "section": "Общий раздел", "exam_code": "ОРТ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 120},
            {"exam": "Общереспубликанское тестирование", "subject": "Грамматика", "section": "Общий раздел", "exam_code": "ОРТ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 120},
            {"exam": "Общереспубликанское тестирование", "subject": "Химия", "section": "Общий раздел", "exam_code": "ОРТ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 150},
            {"exam": "Общереспубликанское тестирование", "subject": "Биология", "section": "Общий раздел", "exam_code": "ОРТ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 150},
            {"exam": "Общереспубликанское тестирование", "subject": "Английский язык", "section": "Общий раздел", "exam_code": "ОРТ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 150},
            {"exam": "Общереспубликанское тестирование", "subject": "Физика", "section": "Общий раздел", "exam_code": "ОРТ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 150},
            {"exam": "Общереспубликанское тестирование", "subject": "История", "section": "Общий раздел", "exam_code": "ОРТ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 150},
            
            # ЕГЭ - экзаменационные предметы
            {"exam": "Единый государственный экзамен", "subject": "Математика", "section": "Общий раздел", "exam_code": "ЕГЭ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 235},
            {"exam": "Единый государственный экзамен", "subject": "Русский язык", "section": "Общий раздел", "exam_code": "ЕГЭ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 210},
            {"exam": "Единый государственный экзамен", "subject": "Химия", "section": "Общий раздел", "exam_code": "ЕГЭ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 180},
            {"exam": "Единый государственный экзамен", "subject": "История", "section": "Общий раздел", "exam_code": "ЕГЭ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 180},
            {"exam": "Единый государственный экзамен", "subject": "Биология", "section": "Общий раздел", "exam_code": "ЕГЭ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 180},
            {"exam": "Единый государственный экзамен", "subject": "Физика", "section": "Общий раздел", "exam_code": "ЕГЭ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 235},
            {"exam": "Единый государственный экзамен", "subject": "Литература", "section": "Общий раздел", "exam_code": "ЕГЭ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 180},
            {"exam": "Единый государственный экзамен", "subject": "Обществознание", "section": "Общий раздел", "exam_code": "ЕГЭ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 180},
            {"exam": "Единый государственный экзамен", "subject": "Информатика", "section": "Общий раздел", "exam_code": "ЕГЭ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 235},
            {"exam": "Единый государственный экзамен", "subject": "География", "section": "Общий раздел", "exam_code": "ЕГЭ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 180},
            {"exam": "Единый государственный экзамен", "subject": "Английский язык", "section": "Общий раздел", "exam_code": "ЕГЭ", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 180},
            
            # SAT - экзаменационные предметы
            {"exam": "Scholastic Assessment Test", "subject": "Math", "section": "General", "exam_code": "SAT", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 180},
            {"exam": "Scholastic Assessment Test", "subject": "English", "section": "General", "exam_code": "SAT", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 180},
            
            # Математика - разделы
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Арифметические действия с числами", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Делимость и простые числа", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Десятичные дроби и проценты", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Линейные уравнения и неравенства", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Квадратные уравнения", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Системы уравнений", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Формулы сокращённого умножения", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Многочлены и действия с ними", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Функции и графики", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Показательные и логарифмические уравнения", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Прогрессии", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Модуль и уравнения с модулем", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Комбинаторика", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Вероятности событий", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Признаки равенства треугольников", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Площадь треугольника и параллелограмма", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Углы и их измерения", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Многоугольники", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Окружность", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Объёмы и площади тел", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Координатная геометрия", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Математика", "section": "Векторы", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            
            # Химия - разделы
            {"exam": "Свободные разделы", "subject": "Химия", "section": "Строение атома", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Химия", "section": "Периодическая система", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Химия", "section": "Валентность и химические формулы", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Химия", "section": "Классификация веществ", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Химия", "section": "Типы химических реакций", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Химия", "section": "Уравнивание реакций", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Химия", "section": "Электролитическая диссоциация", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Химия", "section": "Кислоты, основания и соли", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Химия", "section": "Окислительно-восстановительные реакции", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Химия", "section": "Химические расчёты", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Химия", "section": "Органическая химия", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            
            # Биология - разделы
            {"exam": "Свободные разделы", "subject": "Биология", "section": "Клетка", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Биология", "section": "Деление клетки", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Биология", "section": "Генетика", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Биология", "section": "Органы и системы человека", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Биология", "section": "Обмен веществ", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Биология", "section": "Размножение организмов", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Биология", "section": "Эволюция", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Биология", "section": "Экология", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Биология", "section": "Бактерии и вирусы", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Биология", "section": "Растения", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            
            # География - разделы
            {"exam": "Свободные разделы", "subject": "География", "section": "Координаты и карты", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "География", "section": "Климатические пояса", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "География", "section": "Природные зоны", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "География", "section": "Население мира", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "География", "section": "Политическая карта", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "География", "section": "Природные ресурсы", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "География", "section": "География страны", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            
            # Литература - разделы
            {"exam": "Свободные разделы", "subject": "Литература", "section": "Род и жанр произведения", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Литература", "section": "Главная идея и тема", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Литература", "section": "Анализ героев", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Литература", "section": "Средства выразительности", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Литература", "section": "Эпохи и направления", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Литература", "section": "Сравнение произведений", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Литература", "section": "Авторская позиция", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            
            # Обществознание - разделы
            {"exam": "Свободные разделы", "subject": "Обществознание", "section": "Человек и общество", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Обществознание", "section": "Социальные отношения", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Обществознание", "section": "Политика", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Обществознание", "section": "Право", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Обществознание", "section": "Конституция", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Обществознание", "section": "Экономика", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Обществознание", "section": "Финансовая грамотность", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Обществознание", "section": "Семья и брак", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            
            # Русский язык - разделы
            {"exam": "Свободные разделы", "subject": "Русский язык", "section": "Правописание", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Русский язык", "section": "Пунктуация", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Русский язык", "section": "Синтаксис", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Русский язык", "section": "Морфология", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Русский язык", "section": "Лексика", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Русский язык", "section": "Орфоэпия", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Русский язык", "section": "Стили речи", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Русский язык", "section": "Связь в тексте", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Русский язык", "section": "Редактирование текста", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            
            # Английский язык - разделы
            {"exam": "Свободные разделы", "subject": "Английский язык", "section": "Времена глаголов", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Английский язык", "section": "Пассивный залог", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Английский язык", "section": "Косвенная речь", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Английский язык", "section": "Модальные глаголы", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Английский язык", "section": "Артикли", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Английский язык", "section": "Предлоги", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Английский язык", "section": "Условные предложения", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Английский язык", "section": "Словообразование", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Английский язык", "section": "Чтение", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": "S", "default_question_count": 20, "time_to_complete": 60},
            {"exam": "Свободные разделы", "subject": "Английский язык", "section": "Грамматические задания", "exam_code": "FREE", "has_fixed_structure": False, "default_question_count": 20, "time_to_complete": 60}
        ]

        for section_data in sections:
            try:
                # Check if section already exists to avoid duplicates
                if not Section.objects.filter(
                    exam=section_data['exam'],
                    subject=section_data['subject'],
                    section=section_data['section']
                ).exists():
                    Section.objects.create(**section_data)
                    self.stdout.write(self.style.SUCCESS(
                        f"Successfully added: {section_data['exam']} - {section_data['subject']} - {section_data['section']}"
                    ))
                else:
                    self.stdout.write(self.style.WARNING(
                        f"Skipped (already exists): {section_data['exam']} - {section_data['subject']} - {section_data['section']}"
                    ))
            except Exception as e:
                self.stdout.write(self.style.ERROR(
                    f"Error adding {section_data['exam']} - {section_data['subject']} - {section_data['section']}: {str(e)}"
                ))