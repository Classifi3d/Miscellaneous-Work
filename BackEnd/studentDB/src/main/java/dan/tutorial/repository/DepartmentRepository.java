package dan.tutorial.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import dan.tutorial.entity.Department;

@Repository
public interface DepartmentRepository extends JpaRepository<Department,Long>{

    public Department findByDepartmentName(String departmentName);

    public Department findByDepartmentNameIgnoreCase(String departmentName);

    @Query(value="SELECT * FROM DEPARTMENT ",nativeQuery=true)
    public Department findMyWay();

}
