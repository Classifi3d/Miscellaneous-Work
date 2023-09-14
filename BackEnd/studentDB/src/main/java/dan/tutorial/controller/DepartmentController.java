package dan.tutorial.controller;

import dan.tutorial.error.DepartmentNotFoundException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import dan.tutorial.entity.Department;
import dan.tutorial.service.DepartmentService;

import javax.validation.Valid;
import java.util.List;

@RestController
public class DepartmentController {

    @Autowired
    private DepartmentService departmentService;

    private final Logger LOGGER = LoggerFactory.getLogger(DepartmentController.class);

    @PostMapping(value = "/departments", consumes = "application/json")
    public Department saveDepartment(@Valid @RequestBody Department department){
        // DepartmentService service = new DepartmentServiceImplementation();
        LOGGER.info("Inside saveDepartment of DepartmentController");
        return departmentService.saveDepartment(department);
    }

    @GetMapping(value="/departments",consumes = "application/json")
    public List<Department> fetchAllDepartments(){
        LOGGER.info("Inside fetchAllDepartment of DepartmentController");
        return departmentService.fetchDepartmentList();
    }

    @GetMapping(value="/departments/{id}")
    public Department fetchDepartmentById(@PathVariable("id") Long departmentId) throws DepartmentNotFoundException {
        return departmentService.fetchDepartmentId(departmentId);
    }

    @DeleteMapping(value="/departments/{id}")
    public String deleteDepartmentById(@PathVariable("id") Long departmentId){
        departmentService.deleteDepartmentById(departmentId);
        return "Object Deleted!";
    }

    @PutMapping(value="/departments/{id}")
    public Department updateDepartmentById(@PathVariable("id") Long departmentId,
                                           @RequestBody Department department){
        return departmentService.updateDepartmentById(departmentId, department);
    }

    @GetMapping(value="/departments/name/{name}")
    public Department fetchDepartmentByName(@PathVariable("name") String departmentName){
        return departmentService.fetchDepartmentByName(departmentName);
    }

}
