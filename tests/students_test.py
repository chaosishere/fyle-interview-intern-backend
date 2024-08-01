def test_get_assignments_student_1(client, h_student_1):
    response = client.get(
        '/student/assignments',
        headers=h_student_1
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['student_id'] == 1


def test_get_assignments_student_2(client, h_student_2):
    response = client.get(
        '/student/assignments',
        headers=h_student_2
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['student_id'] == 2


def test_post_assignment_null_content(client, h_student_1):
    """
    failure case: content cannot be null
    """

    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'content': None
        })

    assert response.status_code == 400


def test_post_assignment_student_1(client, h_student_1):
    content = 'ABCD TESTPOST'

    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'content': content
        })

    assert response.status_code == 200

    data = response.json['data']
    assert data['content'] == content
    assert data['state'] == 'DRAFT'
    assert data['teacher_id'] is None


def test_submit_assignment_student_1(client, h_student_1):
    response = client.post(
        '/student/assignments/submit',
        headers=h_student_1,
        json={
            'id': 2,
            'teacher_id': 2
        })

    assert response.status_code == 200

    data = response.json['data']
    assert data['student_id'] == 1
    assert data['state'] == 'SUBMITTED'
    assert data['teacher_id'] == 2


def test_assignment_resubmit_error(client, h_student_1):
    response = client.post(
        '/student/assignments/submit',
        headers=h_student_1,
        json={
            'id': 2,
            'teacher_id': 2
        })
    error_response = response.json
    assert response.status_code == 400
    assert error_response['error'] == 'FyleError'
    assert error_response["message"] == 'only a draft assignment can be submitted'


# Created a failure case test for the endpoint /student/assignments/submit where the assignment is being submitted by a student who is not the owner of the assignment. The test should assert that the response status code is 400 and the error message is 'FyleError' and the message is 'only the owner of the assignment can submit the assignment'.
def test_assignment_submit_not_owner(client, h_student_1):
    """
    failure case: only the owner of the assignment can submit the assignment
    """

    response = client.post(
        '/student/assignments/submit',
        headers=h_student_1,
        json={
            'id': 3,
            'teacher_id': 2
        })
    error_response = response.json
    assert response.status_code == 400
    assert error_response['error'] == 'FyleError'
    assert error_response["message"] == 'This assignment belongs to some other student'

# Create a test case for the endpoint /student/assignments/ whare the assignment is being edited by a student who is not the owner of the assignment. The test should assert that the response status code is 400 and the error message is 'FyleError' and the message is 'This assignment belongs to some other student'.
def test_get_assignments_student_not_owner(client, h_student_1):
    """
    failure case: only the owner of the assignment can view the assignment
    """

    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'id': 3,
            'content': 'ABCD POST'
        })

    assert response.status_code == 400

