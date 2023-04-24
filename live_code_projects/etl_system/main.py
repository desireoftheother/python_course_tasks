from live_code_projects.etl_system.src.extract.csv import CSVExtractor
from live_code_projects.etl_system.src.extract.json import JSONExtractor
from live_code_projects.etl_system.src.transform.filter.filter_by_column_val import FilterByColumnValues
from live_code_projects.etl_system.src.transform.filter.filter_ds_by_another import FilterOneDatasetByAnother
from live_code_projects.etl_system.src.transform.filter.get_one_column import GetOneColumn

titanic_data = CSVExtractor("/home/illia-teacher/PycharmProjects/python_course_tasks/Module_2/"
                            "Lesson 1/titanic_data/titanic_data_2.csv").extract()

survival_data = JSONExtractor("/home/illia-teacher/PycharmProjects/python_course_tasks/Module_2/"
                              "Lesson 1/titanic_data/survival_data.json").extract()

filtered_survivors = FilterByColumnValues(survival_data, {"Survived": "1"}).transform()

survival_id = GetOneColumn(input_dataset=survival_data, column_name="PassengerId").transform()

filtered_dataset = FilterOneDatasetByAnother(main_dataset=titanic_data,
                                             filter_dataset=survival_id,
                                             predicate=lambda main, filter: True if main["PassengerId"] in
                                                                                    [o["PassengerId"] for o in filter]
                                             else False).transform()

print(filtered_dataset)
