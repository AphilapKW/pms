from datetime import datetime
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import WorkOrder, MaidRequest
from django.contrib.auth.models import User


class WorkOrderAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = User.objects.create_user(username="guest1", password="testpassword")
        self.user = User.objects.create_user(username="userservice1", password="testpassword")
        self.client.force_authenticate(user=self.customer)

    def test_create_work_order_failed(self):
        url = reverse("pms:work_order_list")
        data = {
            "room": "101",
            "created_by": self.customer.id,
            "assigned_to": self.user.id,
            "started_at": "2023-05-27T10:00:00",
            "finished_at": None,
            "work_type": "Cleaning",
            "work_status": "Created"
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_work_order(self):
        url = reverse("pms:work_order_list")
        data = {
            "room": "101",
            "work_order_number": "WO001",
            "created_by": self.customer.id,
            "assigned_to": self.user.id,
            "started_at": "2023-05-27T10:00:00",
            "finished_at": None,
            "work_type": "Cleaning",
            "work_status": "Created"
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WorkOrder.objects.count(), 1)
        self.assertEqual(WorkOrder.objects.get().work_order_number, "WO001")

    def test_get_work_order_list(self):
        WorkOrder.objects.create(
            work_order_number="WO002",
            created_by=self.customer,
            assigned_to=self.user,
            room="102",
            started_at=datetime.now(tz=timezone.utc),
            finished_at=None,
            work_type="Cleaning",
            work_status="Created"
        )
        url = reverse("pms:work_order_detail", args=['1'])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["work_order_number"], "WO002")

    def test_patch_work_order_list(self):
        WorkOrder.objects.create(
            work_order_number="WO002",
            created_by=self.customer,
            assigned_to=self.user,
            room="102",
            started_at=datetime.now(tz=timezone.utc),
            finished_at=None,
            work_type="Cleaning",
            work_status="Created"
        )
        data = {
            "work_order_number": "WO002",
            "work_status": "Assigned"
        }
        url = reverse("pms:work_order_detail", args=['1'])
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["work_status"], "Assigned")


class MaidRequestAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = User.objects.create_user(username="guest1", password="testpassword")
        self.user = User.objects.create_user(username="userservice1", password="testpassword")
        self.client.force_authenticate(user=self.customer)
        self.work_order = WorkOrder.objects.create(
            work_order_number="WO002",
            created_by=self.customer,
            assigned_to=self.user,
            room="102",
            started_at=datetime.now(tz=timezone.utc),
            finished_at=None,
            work_type="Cleaning",
            work_status="Created"
        )

    def test_create_maid_request_failed(self):
        url = reverse("pms:maid_request_list")
        data = {
            "description": "clean all"
        }

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_maid_request(self):
        url = reverse("pms:maid_request_list")
        data = {
            "work_order": self.work_order.id,
            "description": "clean all"
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MaidRequest.objects.get().work_order.id, 1)

    def test_get_maid_request_detail(self):
        MaidRequest.objects.create(
            work_order=self.work_order,
            description="clean all"
        )
        url = reverse("pms:maid_request_detail", args=['1'])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["work_order"], 1)

    def test_patch_maid_request_list(self):
        MaidRequest.objects.create(
            work_order=self.work_order,
            description="clean all"
        )
        data = {
            "work_order": self.work_order.id,
            "description": "clean bed"
        }
        url = reverse("pms:maid_request_detail", args=['1'])
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], "clean bed")
