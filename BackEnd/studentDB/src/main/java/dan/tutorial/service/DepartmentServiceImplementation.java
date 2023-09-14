package dan.tutorial.service;

import dan.tutorial.error.DepartmentNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import dan.tutorial.entity.Department;
import dan.tutorial.repository.DepartmentRepository;

import java.util.List;
import java.util.Objects;
import java.util.Optional;

@Service
public class DepartmentServiceImplementation implements DepartmentService{

    @Autowired
    private DepartmentRepository departmentRepository;


    @Override
    public Department saveDepartment(Department department) {
        // TODO Auto-generated method stub
        return departmentRepository.save(department);
    }

    @Override
    public List<Department> fetchDepartmentList() {
        // TODO Auto-generated method stub
        return departmentRepository.findAll();
    }

//    @Override
//    public Department fetchDepartmentId(Long departmentId) {
//        // TODO Auto-generated method stub
//        return departmentRepository.findById(departmentId).get();
//    }
    @Override
    public Department fetchDepartmentId(Long departmentId) throws DepartmentNotFoundException {
        // TODO Auto-generated method stub
        Optional<Department> department = departmentRepository.findById(departmentId);
        if(department.isEmpty()) {
            throw new DepartmentNotFoundException("Department NOT FOUND!");
        }else{
            return department.get();
        }
    }

    @Override
    public void deleteDepartmentById(Long departmentId) {
        // TODO Auto-generated method stub
        departmentRepository.deleteById(departmentId);
    }

    @Override
    public Department updateDepartmentById(Long departmentId, Department department) {
        // TODO Auto-generated method stub
        Department aux = departmentRepository.findById(departmentId).get();

        if(Objects.nonNull(department.getDepartmentName()) &&! "".equalsIgnoreCase(department.getDepartmentName())){
            aux.setDepartmentName(department.getDepartmentName());
        }
        if(Objects.nonNull(department.getDepartmentAddress()) &&! "".equalsIgnoreCase(department.getDepartmentAddress())){
            aux.setDepartmentAddress(department.getDepartmentAddress());
        }
        if(Objects.nonNull(department.getDepartmentCode()) &&! "".equalsIgnoreCase(department.getDepartmentCode())){
            aux.setDepartmentCode(department.getDepartmentCode());
        }
        return departmentRepository.save(aux);
    }

    @Override
    public Department fetchDepartmentByName(String departmentName) {
        // TODO Auto-generated method stub

        return departmentRepository.findByDepartmentNameIgnoreCase(departmentName);
    }

}
