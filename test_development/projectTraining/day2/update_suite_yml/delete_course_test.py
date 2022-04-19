# NOTE: Generated By HttpRunner v3.1.5
# FROM: suite_case\delete_course.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseDeleteCourse(HttpRunner):

    config = Config("删除课程").base_url("http://120.55.190.222:7080").verify(False)

    teststeps = [
        Step(
            RunRequest("删除课程")
            .delete("/api/mgr/sq_mgr/")
            .with_cookies(**{"sessionid": "${cookie}"})
            .with_data({"action": "delete_course", "id": "${course_id}"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.retcode", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseDeleteCourse().test_start()
